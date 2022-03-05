from ariadne import (QueryType, ObjectType)
from .models import *

query = QueryType()
country = ObjectType("Country")
region = ObjectType("Region")
professor = ObjectType("Professor")
professor_course = ObjectType("ProfessorCourse")


@query.field("country")
def resolve_country(_, info, local_language_name=None):
    print(local_language_name)
    if local_language_name:
        try:
            return Country.nodes.get(local_language_name=local_language_name)
        except Country.DoesNotExist:
            return None
    return None


@query.field("allCountries")
def resolve_all_countries(_, info, amount: int = None):
    if amount is None or amount >= len(Region.nodes):
        return Country.nodes.all()
    return Country.nodes.all()[:amount]


@country.field("regions") # the amount argument does not work for country query idk why
@query.field("allRegions")
def resolve_all_regions(_, info, amount: int = None):
    print("in resolve_all_regions, amount = ", amount)
    if amount is None or amount >= len(Region.nodes):
        return Region.nodes.all()
    return Region.nodes.all()[:amount]


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
    return Professor.nodes.all()[:amount]


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
    return ProfessorCourse.nodes.all()[:amount]


@query.field("hello")
def resolve_hello(_, info):  # root resolver
    request = info.context["request"]
    user_agent = request.headers.get("user-agent", "guest")
    return "Hello... %s" % user_agent




