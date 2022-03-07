from neomodel import StructuredNode
from py2neo import Graph, errors
from your_professor.settings import neo4j_login, neo4j_password # ignore red underline, it's all good!


def get_nodes_by_uid_or_none_of(node_class: StructuredNode, uid: str):
    try:
        return node_class.nodes.get(uid=uid)
    except node_class.DoesNotExist:
        return None


def get_amount_or_all_of(node_class: StructuredNode, amount: int):
    if amount is None or amount >= len(node_class.nodes):
        print(node_class.nodes.all())
        return node_class.nodes.all()
    return node_class.nodes.all()[:amount]


def check_database_connection(f):
    def wrapper(*args, **kwargs):
        try:
            Graph("bolt://localhost:7687", auth=(neo4j_login, neo4j_password))
        except errors.ConnectionUnavailable as e:
            raise errors.ConnectionUnavailable("connection to database could not be established")
        return f(*args, **kwargs)
    return wrapper

# def check_database_connection():
#     try:
#         Graph("bolt://localhost:7682", auth=(neo4j_login, neo4j_password))
#     except errors.ConnectionUnavailable as e:
#         raise errors.ConnectionUnavailable("connection to database could not be established")