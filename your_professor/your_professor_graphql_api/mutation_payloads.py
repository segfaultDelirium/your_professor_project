from .models import Country, Region, City, University, Faculty, Specialization, Course


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


def create_mutation_payload_university(status: bool, error: str = None, university: University = None):
    return create_mutation_payload(status, error, "university", university)


def create_mutation_payload_faculty(status: bool, error: str = None, faculty: Faculty = None):
    return create_mutation_payload(status, error, "faculty", faculty)


def create_mutation_payload_specialization(status: bool, error: str = None, specialization: Specialization = None):
    return create_mutation_payload(status, error, "specialization", specialization)


def create_mutation_payload_course(status: bool, error: str = None, course: Course = None):
    return create_mutation_payload(status, error, "course", course)
