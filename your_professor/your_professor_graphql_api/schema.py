from ariadne import (QueryType, ObjectType,
                     gql, make_executable_schema)
from ariadne.asgi import GraphQL
from neomodel import DoesNotExist
import typing
from .models import *
import neomodel

query = QueryType()

type_defs = gql("""
    type Query{
        hello: String!
        country(local_language_name: String): Country
        allRegions(amount: Int): [Region!]
        region(uid: String): Region
    }
    type Country{
        uid: String!
        local_language_name: String!
        ISO_code_name: String!
        is_active: Boolean!
        regions(amount: Int): [Region!]!
    }
    
    type Region{
        uid: String!
        local_language_name: String!
        name: String!
        is_active: Boolean!
        cities: [City!]!
    }
    
    type City{
        uid: String!
        local_language_name: String!
        name: String!
        is_active: Boolean!
        universities: [University!]!
    }
    
    type University{
        uid: String!
        local_language_name: String!
        name: String!
        is_active: Boolean!
        founding_year: Int
        faculties: [Faculty!]!
    }
    
    type Faculty{
        uid: String!
        name: String!
        is_active: Boolean!
    }
    
    type Course{
        uid: String!
        name: String!
        is_active: Boolean!
    }
    
""")

country = ObjectType("Country")


@query.field("country")
def resolve_country(_, info, local_language_name=None):
    print(local_language_name)
    if local_language_name:
        try:
            return Country.nodes.get(local_language_name=local_language_name)
        except Country.DoesNotExist:
            return None
    return None


@country.field("regions") # the amount argument does not work for country query idk why
@query.field("allRegions")
def resolve_all_regions(_, info, amount: int=-1):
    print("in resolve_all_regions, amount = ", amount)
    if amount == -1 or amount >= len(Region.nodes):
        return Region.nodes.all()
    if amount == 0:
        return None
    return Region.nodes.all()[amount:]

# @query.field("region")
# def resolve_region(_, info, uid):
#     if uid:
#         return Region.nodes.get(uid=uid)
#     return None


@query.field("hello")
def resolve_hello(_, info):  # root resolver
    request = info.context["request"]
    user_agent = request.headers.get("user-agent", "guest")
    return "Hello... %s" % user_agent


schema = make_executable_schema(type_defs, query)

app = GraphQL(schema, debug=True)

