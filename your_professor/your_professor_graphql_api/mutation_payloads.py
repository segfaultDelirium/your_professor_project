from .models import Country, Region, City, University, Faculty, Specialization, Course, ProfessorCourse, Professor, \
    ScienceDomain, User, Tag, Review


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


def create_mutation_payload_science_domain(status: bool, error: str = None, science_domain: ScienceDomain = None):
    return create_mutation_payload(status, error, "science_domain", science_domain)


def create_mutation_payload_course(status: bool, error: str = None, course: Course = None):
    return create_mutation_payload(status, error, "course", course)


def create_mutation_payload_professor_course(status: bool, error: str = None, professor_course: ProfessorCourse = None):
    return create_mutation_payload(status, error, "professor_course", professor_course)


def create_mutation_payload_professor(status: bool, error: str = None, professor: Professor = None):
    return create_mutation_payload(status, error, "professor", professor)


def create_mutation_payload_user(status: bool, error: str = None, user: User = None):
    return create_mutation_payload(status, error, "user", user)


def create_mutation_payload_tag(status: bool, error: str = None, tag: Tag = None):
    return create_mutation_payload(status, error, "tag", tag)


def create_mutation_payload_review(status: bool, error: str = None, review: Review = None):
    return create_mutation_payload(status, error, "review", review)