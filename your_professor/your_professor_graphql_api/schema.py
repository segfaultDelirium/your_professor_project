from ariadne import (ScalarType, make_executable_schema)
from ariadne.asgi import GraphQL
from .resolvers.schema_field_settings import (mutation, query, country, region, city, university, faculty,
                                              specialization, science_domain, course, professor_course, professor,
                                              user, teaches_details )
from .type_defs import type_defs
datetime_scalar = ScalarType("Datetime")


@datetime_scalar.serializer
def serialize_datetime(value):
    return value.isoformat()


schema = make_executable_schema(type_defs,
                                query,
                                mutation,
                                country,
                                region,
                                city,
                                university,
                                faculty,
                                specialization,
                                science_domain,
                                course,
                                professor,
                                # teaches_details,
                                user,
                                datetime_scalar)

app = GraphQL(schema, debug=True)
