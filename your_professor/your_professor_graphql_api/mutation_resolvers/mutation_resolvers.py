from ariadne import (MutationType)

from .mutation_resolvers_city import resolve_create_city, resolve_update_city, resolve_delete_city
from .mutation_resolvers_country import (resolve_create_country_by_ISO,
                                         resolve_update_country, resolve_delete_country)
from .mutation_resolvers_region import (resolve_update_region, resolve_create_region, resolve_delete_region)
from .mutation_resolvers_university import resolve_create_university, resolve_update_university, \
    resolve_delete_university

mutation = MutationType()
mutation.set_field("createCountryByISO", resolve_create_country_by_ISO)
mutation.set_field("updateCountry", resolve_update_country)
mutation.set_field("deleteCountry", resolve_delete_country)

mutation.set_field("createRegion", resolve_create_region)
mutation.set_field("updateRegion", resolve_update_region)
mutation.set_field("deleteRegion", resolve_delete_region)

mutation.set_field("createCity", resolve_create_city)
mutation.set_field("updateCity", resolve_update_city)
mutation.set_field("deleteCity", resolve_delete_city)

mutation.set_field("createUniversity", resolve_create_university)
mutation.set_field("updateUniversity", resolve_update_university)
mutation.set_field("deleteUniversity", resolve_delete_university)

