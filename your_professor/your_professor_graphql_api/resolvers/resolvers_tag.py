from ..models import Tag
from ..mutation_payloads import create_mutation_payload_tag, create_mutation_payload
from .resolver_utils import (get_amount_or_all_of, get_nodes_by_uid_or_none_of, check_database_connection,
                             check_birthday_format)


@check_database_connection
def resolve_tag(obj, info, uid=None):
    if obj is not None:
        return obj.tag.all()[0]
    return get_nodes_by_uid_or_none_of(Tag, uid)


@check_database_connection
def resolve_all_tags(obj, info, amount: int = None):
    if obj is not None:
        if amount is None or amount >= len(obj.tags):
            return obj.tags.all()
        return obj.tags.all()[:amount]
    return get_amount_or_all_of(Tag, amount)


def resolve_create_tag(_, info, tag: str):
    try:
        Tag.nodes.get(tag=tag)
        return create_mutation_payload(False, error=f"{tag=} of this label already exists")
    except Tag.DoesNotExist:
        pass
    try:
        new_tag = Tag(tag=tag).save()
        return create_mutation_payload_tag(True, tag=new_tag)
    except Exception as e:
        print(e)
        return create_mutation_payload(False, error="Sum ting wong")


def resolve_update_tag(_, info, uid:str, tag: str):
    try:
        Tag.nodes.get(tag=tag)
        return create_mutation_payload(False, error="Tag with this label was already created")
    except Tag.DoesNotExist:
        pass
    try:
        tag_ref = Tag.nodes.get(uid=uid)
        tag_ref.tag = tag
        tag_ref.save()
        return create_mutation_payload_tag(True, tag=tag_ref)
    except Tag.DoesNotExist:
        return create_mutation_payload(False, error=f'tag with {uid=} could not be found')


def resolve_delete_tag(_, info, uid: str):
    try:
        Tag.nodes.get(uid=uid).delete()
        return create_mutation_payload(True)
    except Tag.DoesNotExist:
        return create_mutation_payload(False, error=f'tag with {uid=} could not be found')
