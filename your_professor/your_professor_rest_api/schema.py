from ariadne import (QueryType, ObjectType,
                     gql, make_executable_schema)
from ariadne.asgi import GraphQL
from .models import *

query = QueryType()

type_defs = gql("""
    type Query{
        hello: String!
        country(local_language_name: String): Country
    }
    type Country{
        uid: String!
        local_language_name: String!
        ISO_code_name: String!
        is_active: Boolean
    }
""")


@query.field("country")
def resolve_country(_, info, local_language_name=None):
    print(local_language_name)
    polska = Country.nodes.get(local_language_name="Polska")
    print(polska)
    return polska


@query.field("hello")
def resolve_hello(_, info):  # root resolver
    request = info.context["request"]
    user_agent = request.headers.get("user-agent", "guest")
    return "Hello... %s" % user_agent


schema = make_executable_schema(type_defs, query)

app = GraphQL(schema, debug=True)

