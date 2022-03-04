import neomodel.exceptions
from ariadne import (QueryType, ObjectType, MutationType)
from .models import *

query = QueryType()

country = ObjectType("Country")
region = ObjectType("Region")
professor = ObjectType("Professor")


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


@query.field("region")
def resolve_region(_, info, uid):
    if uid:
        return Region.nodes.get(uid=uid)
    return None


@region.field("country")
def resolve_region_country(obj, info):
    print("obj = ", obj)
    print("info = ", info)
    print("obj.country ", obj.country.all())
    # print("obj.country.local_language_name ",obj.country.local_language_name)
    return obj.country.all()[0]


@query.field("allProfessors")
def resolve_all_professors(_, info, amount: int=-1):
    print("in resolve_all_professors, amount = ", amount)
    if amount == -1 or amount >= len(Region.nodes):
        return Professor.nodes.all()
    if amount == 0:
        return None
    return Professor.nodes.all()[amount:]


professor_course = ObjectType("ProfessorCourse")


@professor_course.field("professor")
def resolve_professor_course_professor(object, info):
    print("in resolve_professor_course_professor")
    print(object)
    print(info)
    return None


@query.field("allProfessorCourses")
def resolve_all_professor_courses(_, info, amount: int=-1):
    print(info.context['request'])
    print("in resolve_all_professor_courses, amount = ", amount)
    if amount == -1 or amount >= len(Region.nodes):
        return ProfessorCourse.nodes.all()
    if amount == 0:
        return None
    return ProfessorCourse.nodes.all()[amount:]


@query.field("hello")
def resolve_hello(_, info):  # root resolver
    request = info.context["request"]
    user_agent = request.headers.get("user-agent", "guest")
    return "Hello... %s" % user_agent


mutation = MutationType()


@mutation.field("updateRegion")
def resolve_update_region(_, info, uid, local_language_name=None, name=None, is_active=None):
    print(uid)
    try:
        this_region = Region.nodes.get(uid=uid)
        if local_language_name is None or local_language_name == "":
            this_region.local_language_name = local_language_name
        if name is None or name == "": this_region.name = name
        if is_active is None: this_region.is_active = is_active
        this_region.save()
    except Region.DoesNotExist:
        return False

    return True


# @mutation.field("connectRegionToCountry")
# def resolve_connect_region_to_country(_, info, uid, country_uid):
#     try:
#         this_region = Region.nodes.get(uid=uid)
#         this_country = Country.nodes.get(uid=country_uid)
#         this_region.country.connect(this_country)
#     except Region.DoesNotExist:
#         return {"status": False, "error": f"Region of {uid=} does not exist."}
#     except Country.DoesNotExist:
#         return {"status": False, "error": f"Country of {country_uid=} does not exist."}
#     except neomodel.exceptions.AttemptedCardinalityViolation as ACV:
#         return {"status": False, "error": f"Region can only be connected to one Country."}
#     this_region.save()
#     return {"status": True}


@mutation.field("reconnectRegionToCountry")
def resolve_reconnect_region_to_country(_, info, uid, country_uid):
    try:
        this_region = Region.nodes.get(uid=uid)
        this_country = Country.nodes.get(uid=country_uid)
        if this_country != this_region.country.all()[0]: this_region.country.reconnect(this_country)
    except Region.DoesNotExist:
        return {"status": False, "error": f"Region of {uid=} does not exist."}
    this_region.save()
    return {"status": True}


@mutation.field("createCountryByISO")
def resolve_create_country_by_ISO(_, info, local_language_name: str, ISO_code_name: str):
    if COUNTRIES.get(ISO_code_name) is None:
        return create_mutation_payload(False, "Incorrect ISO code")
    print(COUNTRIES.get(ISO_code_name))
    try:
        probing_country = Country.nodes.get(ISO_code_name=ISO_code_name)
        return create_mutation_payload(False, "Country with this ISO code already exist")
    except Country.DoesNotExist as e:
        pass
    try:
        new_country = Country(local_language_name=local_language_name, ISO_code_name=ISO_code_name).save()
        return {"status": True}
    except Exception as e:
        print(e)
        return {"status": False, "error": "Sum ting Wong"}


@mutation.field("updateCountry")
def resolve_update_country(_, info, uid: str, local_language_name: str, ISO_code_name: str, is_active: bool):
    print(uid)
    try:
        this_country = Country.nodes.get(uid=uid)
        if local_language_name is None or local_language_name == "":
            this_country.local_language_name = local_language_name
        if ISO_code_name is None or ISO_code_name == "": this_country.ISO_code_name = ISO_code_name
        if is_active is None: this_country.is_active = is_active
        this_country.save()
    except Region.DoesNotExist:
        return create_mutation_payload(False, "Country you are trying to modify does not exist")

    return create_mutation_payload(True)



def create_mutation_payload(status: bool, error: str = None):
    return {
        "status": status,
        "error": error
    }