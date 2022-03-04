from ariadne import (MutationType)
from .mutation_resolvers_country import (resolve_create_country_by_ISO,
                                         resolve_update_country, resolve_delete_country)
from .mutation_resolvers_region import resolve_update_region, resolve_reconnect_region_to_country, resolve_create_region

mutation = MutationType()
mutation.set_field("createCountryByISO", resolve_create_country_by_ISO)
mutation.set_field("updateCountry", resolve_update_country)
mutation.set_field("updateRegion", resolve_update_region)
mutation.set_field("reconnectRegionToCountry", resolve_reconnect_region_to_country)
mutation.set_field("createRegion", resolve_create_region)
mutation.set_field("deleteCountry", resolve_delete_country)