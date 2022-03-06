from ariadne import (MutationType, QueryType, ObjectType)

from .resolvers_city import resolve_create_city, resolve_update_city, resolve_delete_city, resolve_all_cities, \
    resolve_city
from .resolvers_country import (resolve_create_country_by_ISO,
                                resolve_update_country, resolve_delete_country, resolve_country, resolve_all_countries)
from .resolvers_course import resolve_create_course, resolve_delete_course, resolve_update_course
from .resolvers_faculty import resolve_create_faculty, resolve_update_faculty, resolve_delete_faculty
from .resolvers_professor import resolve_create_professor, resolve_delete_professor, resolve_update_professor, \
    resolve_connect_professor_to_professor_course, resolve_reconnect_professor_to_professor_course, \
    resolve_disconnect_professor_from_professor_course, resolve_all_professors, resolve_professor_course_professor
from .resolvers_professor_course import resolve_create_professor_course, resolve_update_professor_course, \
    resolve_delete_professor_course, resolve_all_professor_courses
from .resolvers_region import (resolve_update_region, resolve_create_region, resolve_delete_region, resolve_region,
                               resolve_all_regions)
from .resolvers_specialization import resolve_create_specialization, resolve_delete_specialization, \
    resolve_update_specialization
from .resolvers_university import resolve_create_university, resolve_update_university, \
    resolve_delete_university

query = QueryType()
mutation = MutationType()
country = ObjectType("Country")
region = ObjectType("Region")
city = ObjectType("City")

professor = ObjectType("Professor")
professor_course = ObjectType("ProfessorCourse")

query.set_field("country", resolve_country)
region.set_field("country", resolve_country)
query.set_field("allCountries", resolve_all_countries)
mutation.set_field("createCountryByISO", resolve_create_country_by_ISO)
mutation.set_field("updateCountry", resolve_update_country)
mutation.set_field("deleteCountry", resolve_delete_country)

query.set_field("region", resolve_region)
city.set_field("region", resolve_region)
query.set_field("allRegions", resolve_all_regions)
country.set_field("regions", resolve_all_regions)
mutation.set_field("createRegion", resolve_create_region)
mutation.set_field("updateRegion", resolve_update_region)
mutation.set_field("deleteRegion", resolve_delete_region)

query.set_field("city", resolve_city)
query.set_field("allCities", resolve_all_cities)
region.set_field("cities", resolve_all_cities)
mutation.set_field("createCity", resolve_create_city)
mutation.set_field("updateCity", resolve_update_city)
mutation.set_field("deleteCity", resolve_delete_city)

mutation.set_field("createUniversity", resolve_create_university)
mutation.set_field("updateUniversity", resolve_update_university)
mutation.set_field("deleteUniversity", resolve_delete_university)

mutation.set_field("createFaculty", resolve_create_faculty)
mutation.set_field("updateFaculty", resolve_update_faculty)
mutation.set_field("deleteFaculty", resolve_delete_faculty)

mutation.set_field("createSpecialization", resolve_create_specialization)
mutation.set_field("updateSpecialization", resolve_update_specialization)
mutation.set_field("deleteSpecialization", resolve_delete_specialization)

mutation.set_field("createCourse", resolve_create_course)
mutation.set_field("updateCourse", resolve_update_course)
mutation.set_field("deleteCourse", resolve_delete_course)

query.set_field("allProfessorCourses", resolve_all_professor_courses)
mutation.set_field("createProfessorCourse", resolve_create_professor_course)
mutation.set_field("updateProfessorCourse", resolve_update_professor_course)
mutation.set_field("deleteProfessorCourse", resolve_delete_professor_course)

query.set_field("allProfessors", resolve_all_professors)
professor_course.set_field("professor", resolve_professor_course_professor)
mutation.set_field("createProfessor", resolve_create_professor)
mutation.set_field("updateProfessor", resolve_update_professor)
mutation.set_field("connectProfessorToProfessorCourse", resolve_connect_professor_to_professor_course)
mutation.set_field("reconnectProfessorToProfessorCourse", resolve_reconnect_professor_to_professor_course)
mutation.set_field("disconnectProfessorFromProfessorCourse", resolve_disconnect_professor_from_professor_course)
mutation.set_field("deleteProfessor", resolve_delete_professor)