from neomodel import StructuredNode


def get_nodes_by_uid_or_none_of(node_class: StructuredNode, uid: str):
    try:
        return node_class.nodes.get(uid=uid)
    except node_class.DoesNotExist:
        return None


def get_amount_or_all_of(node_class: StructuredNode, amount: int):
    if amount is None or amount >= len(node_class.nodes):
        return node_class.nodes.all()
    return node_class.nodes.all()[:amount]
