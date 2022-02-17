from ariadne import (QueryType, ObjectType,
                     gql, make_executable_schema)
from ariadne.asgi import GraphQL
from models import *

query = QueryType()

type_defs = gql("""
    type Query{
        hello: String!
        country: Country
    }
    type Country{
        local_language_name: String!
    }
""")

country = ObjectType("Country")


@query.field("country")
def resolve_country(_, info):
    return "hello"


@country.field("local_language_name")
def resolve_local_language_name(obj, *_):
    # print(obj)
    # Country.nodes.get(ISO_code_name="PL")
    # print(Country.nodes.all())
    # user = User.nodes.get(last_name="Charliee")
    # print(user.date_joined)
    return "spain"


@query.field("hello")
def resolve_hello(_, info):  # root resolver
    request = info.context["request"]
    user_agent = request.headers.get("user-agent", "guest")
    return "Hello... %s" % user_agent


schema = make_executable_schema(type_defs, query, country)

app = GraphQL(schema, debug=True)

