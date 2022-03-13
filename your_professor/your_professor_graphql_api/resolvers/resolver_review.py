from ..models import Tag, Review, User, ReviewableNode, Specialization
from ..mutation_payloads import create_mutation_payload_review, create_mutation_payload
from .resolver_utils import (get_amount_or_all_of, get_nodes_by_uid_or_none_of, check_database_connection)
from neomodel.exceptions import DeflateError
from ..constants import DIFFICULTY, QUALITY, REVIEWED_NODE_TYPE


def get_key_of_dict(dict, value):
    for key, val in dict.items():
        if val == value:
            return key


@check_database_connection
def resolve_review(obj, info, uid=None):
    if obj is not None:
        return obj.review.all()[0]
    return get_nodes_by_uid_or_none_of(Review, uid)


@check_database_connection
def resolve_all_reviews(obj, info, amount: int = None):
    if obj is not None:
        if amount is None or amount >= len(obj.reviews):
            return obj.reviews.all()
        return obj.reviews.all()[:amount]
    return get_amount_or_all_of(Review, amount)


def get_node_to_connect(reviewed_node_type, uid):
    try:
        node = eval(f'{reviewed_node_type}.nodes.get(uid="{uid}")')
        return node
    except ReviewableNode.DoesNotExist as e:
        return None


def get_tags_by_uid(tags_uids):
    res = list()
    for uid in tags_uids:
        try:
            res.append(Tag.nodes.get(uid=uid))
        except Tag.DoesNotExist as e:
            raise Tag.DoesNotExist(f"Tag of {uid=} does not exist")
    return res


def resolve_create_review(_, info, is_text_visible: bool = None, text: str = None, quality: str = None,
                          difficulty: str = None, uid_author: str = None, tags = None, reviewed_node_type: str = None,
                          reviewed_node_uid: str = None):
    try:
        author = User.nodes.get(uid=uid_author)
        node_to_connect = get_node_to_connect(reviewed_node_type, reviewed_node_uid)
        if node_to_connect is None:
            return create_mutation_payload(False, error=f"node to review of type {reviewed_node_type} and "
                                                        f"uid {reviewed_node_uid} could not be found.")
        tags = get_tags_by_uid(tags)
        review = Review(is_text_visible=is_text_visible, text=text, quality=quality,
                        difficulty=difficulty,
                        reviewed_node_type=get_key_of_dict(REVIEWED_NODE_TYPE, reviewed_node_type)).save()
        review.author.connect(author)
        review.reviewed_node.connect(node_to_connect)
        for tag in tags:
            review.tags.connect(tag)
        review.save()
        return create_mutation_payload_review(True, review=review)
    except User.DoesNotExist as e:
        print(e)
        return create_mutation_payload(False, error=f"user of {uid_author=} could not be found.")
    except Tag.DoesNotExist as e:
        return create_mutation_payload(False, error=e)
    except DeflateError as e:
        return create_mutation_payload(False, error="invalid choice of quality or difficulty, available choices:"
                                       f"{QUALITY=}, {DIFFICULTY=}")
    except Exception as e:
        print(e)
        return create_mutation_payload(False, error="Sum ting wong")


def resolve_update_review(_, info, uid: str, is_text_visible: bool = None, text: str = None, quality: str = None,
                          difficulty: str = None, tags = None):
    try:
        review = Review.nodes.get(uid=uid)
        tags = get_tags_by_uid(tags)
        if is_text_visible is not None: review.is_text_visible = is_text_visible
        if text is not None: review.text = text
        if quality is not None: review.quality = quality
        if difficulty is not None: review.difficulty = difficulty
        review.tags.disconnect_all()
        for tag in tags:
            review.tags.connect(tag)
        review.save()
        return create_mutation_payload_review(True, review=review)
    except Review.DoesNotExist:
        return create_mutation_payload(False, error=f'Review with {uid=} could not be found')
    except Tag.DoesNotExist as e:
        return create_mutation_payload(False, error=e)
    except DeflateError as e:
        return create_mutation_payload(False, error="invalid choice of quality or difficulty, available choices:"
                                       f"{QUALITY=}, {DIFFICULTY=}")
    except Exception as e:
        print(e)
        return create_mutation_payload(False, error="Sum ting wong")


def resolve_delete_review(_, info, uid: str):
    try:
        Review.nodes.get(uid=uid).delete()
        return create_mutation_payload(True)
    except Review.DoesNotExist:
        return create_mutation_payload(False, error=f'Review with {uid=} could not be found')


# def resolve_connect_review_to_tag(uid_review, uid_tag):
#     try:
#         review = Review.nodes.get(uid=uid_review)
#         tag = Tag.nodes.get(uid=uid_tag)
#         review.tags.connect(tag)
#     except Review.DoesNotExist:
#         return create_mutation_payload(False, error=f'Review with {uid_review=} could not be found')
#     except Tag.DoesNotExist as e:
#         return create_mutation_payload(False, error=e)
#
#
# def resolve_disconnect_review_from_tag(uid_review, uid_tag):
#     try:
#         review = Review.nodes.get(uid=uid_review)
#         tag = Tag.nodes.get(uid=uid_tag)
#         review.tags.disconnect(tag)
#     except Review.DoesNotExist:
#         return create_mutation_payload(False, error=f'Review with {uid_review=} could not be found')
#     except Tag.DoesNotExist as e:
#         return create_mutation_payload(False, error=e)