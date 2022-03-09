from ..models import Tag, Review, User
from ..mutation_payloads import create_mutation_payload_review, create_mutation_payload
from .resolver_utils import (get_amount_or_all_of, get_nodes_by_uid_or_none_of, check_database_connection)
from neomodel.exceptions import DeflateError
from ..constants import DIFFICULTY, QUALITY

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


def resolve_create_review(_, info, is_text_visible: bool = None, text: str = None, quality: str = None,
                          difficulty: str = None, uid_author: str = None, tags = None):
    try:
        author = User.nodes.get(uid=uid_author)
        review = Review(is_text_visible=is_text_visible, text=text, quality=quality,
                        difficulty=difficulty).save()
        # review = Review(is_text_visible=is_text_visible, text=text, quality=f'{quality}',
        #                 difficulty=f'{difficulty}').save()
        review.author.connect(author)
        review.save()
        return create_mutation_payload_review(True, review=review)
    except User.DoesNotExist as e:
        print(e)
        return create_mutation_payload(False, error=f"user of {uid_author=} could not be found.")
    except DeflateError as e:
        return create_mutation_payload(False, error="invalid choice of quality or difficulty, available choices:"
                                       f"{QUALITY=}, {DIFFICULTY=}")
    # except Exception as e:
    #     print(e)
    #     return create_mutation_payload(False, error="Sum ting wong")

#
# def resolve_update_tag(_, info, uid:str, tag: str):
#     try:
#         Tag.nodes.get(tag=tag)
#         return create_mutation_payload(False, error="Tag with this label was already created")
#     except Tag.DoesNotExist:
#         pass
#     try:
#         tag_ref = Tag.nodes.get(uid=uid)
#         tag_ref.tag = tag
#         tag_ref.save()
#         return create_mutation_payload_tag(True, tag=tag_ref)
#     except Tag.DoesNotExist:
#         return create_mutation_payload(False, error=f'tag with {uid=} could not be found')
#
#
# def resolve_delete_tag(_, info, uid: str):
#     try:
#         Tag.nodes.get(uid=uid).delete()
#         return create_mutation_payload(True)
#     except Tag.DoesNotExist:
#         return create_mutation_payload(False, error=f'tag with {uid=} could not be found')