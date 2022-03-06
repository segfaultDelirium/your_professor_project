from ariadne import (MutationType, QueryType, ObjectType)

from .resolvers_city import resolve_create_city, resolve_update_city, resolve_delete_city, resolve_all_cities, \
    resolve_city
from .resolvers_country import (resolve_create_country_by_ISO,
                                resolve_update_country, resolve_delete_country, resolve_country, resolve_all_countries)
from .resolvers_course import resolve_create_course, resolve_delete_course, resolve_update_course, resolve_course, \
    resolve_all_courses
from .resolvers_faculty import resolve_create_faculty, resolve_update_faculty, resolve_delete_faculty, resolve_faculty, \
    resolve_all_faculties
from .resolvers_professor import resolve_create_professor, resolve_delete_professor, resolve_update_professor, \
    resolve_connect_professor_to_professor_course, resolve_reconnect_professor_to_professor_course, \
    resolve_disconnect_professor_from_professor_course, resolve_all_professors, resolve_professor_course_professor
from .resolvers_professor_course import resolve_create_professor_course, resolve_update_professor_course, \
    resolve_delete_professor_course, resolve_all_professor_courses
from .resolvers_region import (resolve_update_region, resolve_create_region, resolve_delete_region, resolve_region,
                               resolve_all_regions)
from .resolvers_science_domain import resolve_science_domain, resolve_all_science_domains, \
    resolve_create_science_domain, resolve_update_science_domain, resolve_delete_science_domain, \
    resolve_connect_science_domain_to_specialization, resolve_disconnect_science_domain_from_specialization
from .resolvers_specialization import resolve_create_specialization, resolve_delete_specialization, \
    resolve_update_specialization, resolve_specialization, resolve_all_specialization
from .resolvers_university import resolve_create_university, resolve_update_university, \
    resolve_delete_university, resolve_university, resolve_all_universities

query = QueryType()
mutation = MutationType()
country = ObjectType("Country")
region = ObjectType("Region")
city = ObjectType("City")
university = ObjectType("University")
faculty = ObjectType("Faculty")
specialization = ObjectType("Specialization")
science_domain = ObjectType("ScienceDomain")
course = ObjectType("Course")

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
mutation.set_field("createRegion", resolve_create_region)
mutation.set_field("updateRegion", resolve_update_region)
mutation.set_field("deleteRegion", resolve_delete_region)

query.set_field("city", resolve_city)
university.set_field("city", resolve_city)
query.set_field("allCities", resolve_all_cities)
region.set_field("cities", resolve_all_cities)
mutation.set_field("createCity", resolve_create_city)
mutation.set_field("updateCity", resolve_update_city)
mutation.set_field("deleteCity", resolve_delete_city)

query.set_field("university", resolve_university)
faculty.set_field("university", resolve_university)
query.set_field("allUniversities", resolve_all_universities)
city.set_field("universities", resolve_all_universities)
mutation.set_field("createUniversity", resolve_create_university)
mutation.set_field("updateUniversity", resolve_update_university)
mutation.set_field("deleteUniversity", resolve_delete_university)

query.set_field("faculty", resolve_faculty)
specialization.set_field("faculty", resolve_faculty)
query.set_field("allFaculties", resolve_all_faculties)
university.set_field("faculties", resolve_all_faculties)
mutation.set_field("createFaculty", resolve_create_faculty)
mutation.set_field("updateFaculty", resolve_update_faculty)
mutation.set_field("deleteFaculty", resolve_delete_faculty)

query.set_field("specialization", resolve_specialization)
query.set_field("allSpecializations", resolve_all_specialization)
faculty.set_field("specializations", resolve_all_specialization)
course.set_field("specializations", resolve_all_specialization)
science_domain.set_field("specializations", resolve_all_specialization)
mutation.set_field("createSpecialization", resolve_create_specialization)
mutation.set_field("updateSpecialization", resolve_update_specialization)
mutation.set_field("deleteSpecialization", resolve_delete_specialization)

query.set_field("scienceDomain", resolve_science_domain)
query.set_field("allScienceDomains", resolve_all_science_domains)
mutation.set_field("createScienceDomain", resolve_create_science_domain)
mutation.set_field("updateScienceDomain", resolve_update_science_domain)
mutation.set_field("connectScienceDomainToSpecialization", resolve_connect_science_domain_to_specialization)
mutation.set_field("disconnectScienceDomainFromSpecialization", resolve_disconnect_science_domain_from_specialization)
mutation.set_field("deleteScienceDomain", resolve_delete_science_domain)

query.set_field("course", resolve_course)
query.set_field("allCourses", resolve_all_courses)
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
