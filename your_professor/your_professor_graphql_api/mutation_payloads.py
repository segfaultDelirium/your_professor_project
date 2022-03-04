from .models import Country, Region, City

def create_mutation_payload(status: bool, error: str = None, data_type: str = None, data = None):
    if data_type:
        return {
            "status": status,
            "error": error,
            f"{data_type}": data
        }
    return {
        "status": status,
        "error": error
    }


def create_mutation_payload_country(status: bool, error: str = None, country: Country = None):
    return create_mutation_payload(status, error, "country", country)


def create_mutation_payload_region(status: bool, error: str = None, region: Region = None):
    return create_mutation_payload(status, error, "region", region)


def create_mutation_payload_city(status: bool, error: str = None, city: City = None):
    return create_mutation_payload(status, error, "city", city)
