from ..models import User, Professor
from ..mutation_payloads import create_mutation_payload, \
    create_mutation_payload_professor
from .resolver_utils import get_amount_or_all_of, get_nodes_by_uid_or_none_of, check_database_connection


@check_database_connection
def resolve_user(obj, info, uid=None):
    if obj is not None:
        return obj.user.all()[0]
    return get_nodes_by_uid_or_none_of(User, uid)


@check_database_connection
def resolve_all_users(obj, info, amount: int = None):
    if obj is not None:
        if amount is None or amount >= len(obj.users):
            return obj.users.all()
        return obj.users.all()[:amount]
    return get_amount_or_all_of(User, amount)
#
#
# def resolve_create_professor(_, info, first_name: str, last_name: str, is_active: bool = None, birth_year: int = None,
#                              is_male: bool = None, degree: str = None, uid_professor_course: str = None):
#     try:
#         professor_course_to_connect = None
#         if uid_professor_course is not None:
#             professor_course_to_connect = ProfessorCourse.nodes.get(uid=uid_professor_course)
#         new_professor = Professor(first_name=first_name, last_name=last_name, is_active=is_active,
#                                   birth_year=birth_year, is_male=is_male, degree=degree).save()
#         if professor_course_to_connect is not None:
#             new_professor.professor_course.connect(professor_course_to_connect)
#         new_professor.save()
#         return create_mutation_payload_professor(True, professor=new_professor)
#     except ProfessorCourse.DoesNotExist as e:
#         print(e)
#         return create_mutation_payload(False,
#                                        error=f"ProfessorCourse of uid {uid_professor_course} could not be found.")
#     except Exception as e:
#         print(e)
#         return create_mutation_payload(False, error="Sum ting wong")
#
#
# def resolve_update_professor(_, info, uid: str, first_name: str = None, last_name: str = None, is_active: bool = None,
#                              birth_year: int = None, is_male: bool = None, degree: str = None,
#                              uid_professor_course: str = None):
#     try:
#         professor = Professor.nodes.get(uid=uid)
#         if first_name is not None and first_name != "":
#             professor.first_name = first_name
#         if last_name is not None and last_name != "":
#             professor.last_name = last_name
#         if is_active is not None:
#             professor.is_active = is_active
#         if birth_year is not None:
#             professor.birth_year = birth_year
#         if is_male is not None:
#             professor.is_male = is_male
#         if degree is not None:
#             professor.degree = degree
#         professor.save()
#         if uid_professor_course is not None:
#             professor_course = ProfessorCourse.nodes.get(uid=uid_professor_course)
#             old_professor_course = professor.professor_course.all()[0]
#             if old_professor_course is None:
#                 professor.professor_course.connect(new_node=professor_course)
#                 professor.save()
#             elif old_professor_course.uid == professor_course.uid:
#                 pass
#             else:
#                 professor.professor_course.reconnect(old_node=old_professor_course, new_node=professor_course)
#                 professor.save()
#         return create_mutation_payload_professor(True, professor=professor)
#     except Professor.DoesNotExist:
#         return create_mutation_payload(False, error=f"Professor of uid {uid} could not be found.")
#     except ProfessorCourse.DoesNotExist:
#         return create_mutation_payload(False,
#                                        error=f"ProfessorCourse of uid {uid_professor_course} could not be found.")
#
#
# def resolve_connect_professor_to_professor_course(_, info, uid: str, uid_professor_course: str):
#     try:
#         professor = Professor.nodes.get(uid=uid)
#         professor_course = ProfessorCourse.nodes.get(uid=uid_professor_course)
#         professor.professor_course.connect(professor_course)
#         professor.save()
#         return create_mutation_payload_professor(True, professor=professor)
#     except Professor.DoesNotExist:
#         return create_mutation_payload(False, error=f"Professor of uid {uid} could not be found.")
#     except ProfessorCourse.DoesNotExist:
#         return create_mutation_payload(False,
#                                        error=f"ProfessorCourse of uid {uid_professor_course} could not be found.")
#
#
# def resolve_reconnect_professor_to_professor_course(_, info, uid: str, uid_old_professor_course: str,
#                                                     uid_new_professor_course: str):
#     old_professor_course = None
#     try:
#         old_professor_course = ProfessorCourse.nodes.get(uid=uid_old_professor_course)
#     except ProfessorCourse.DoesNotExist:
#         return create_mutation_payload(False,
#                                        error=f"Old ProfessorCourse of uid {uid_old_professor_course} "
#                                              "could not be found.")
#     try:
#         professor = Professor.nodes.get(uid=uid)
#         new_professor_course = ProfessorCourse.nodes.get(uid=uid_new_professor_course)
#         professor.professor_courses.reconnect(old_node=old_professor_course, new_node=new_professor_course)
#         professor.save()
#         return create_mutation_payload_professor(True, professor=professor)
#     except Professor.DoesNotExist:
#         return create_mutation_payload(False, error=f"Professor of uid {uid} could not be found.")
#     except ProfessorCourse.DoesNotExist:
#         return create_mutation_payload(False,
#                                        error=f"New ProfessorCourse of uid {uid_old_professor_course} "
#                                              "could not be found.")
#
#
# def resolve_disconnect_professor_from_professor_course(_, info, uid: str, uid_professor_course: str):
#     try:
#         professor = Professor.nodes.get(uid=uid)
#         professor_course = ProfessorCourse.nodes.get(uid=uid_professor_course)
#         professor.professor_courses.disconnect(professor_course)
#         professor.save()
#         return create_mutation_payload_professor(True, professor=professor)
#     except Professor.DoesNotExist:
#         return create_mutation_payload(False, error=f"Professor of uid {uid} could not be found.")
#     except ProfessorCourse.DoesNotExist:
#         return create_mutation_payload(False,
#                                        error=f"ProfessorCourse of uid {uid_professor_course} could not be found.")
#
#
# def resolve_delete_professor(_, info, uid: str, force: bool = False):
#     try:
#         professor = Professor.nodes.get(uid=uid)
#         if not force and len(professor.professor_courses.all()) != 0:
#             return create_mutation_payload(False,
#                                            "Professor you are trying to delete has Courses attached, "
#                                            "please disconnect them before deleting it.")
#         professor.delete()
#         return create_mutation_payload(True)
#     except Professor.DoesNotExist:
#         return create_mutation_payload(False, "Professor you are trying to delete does not exist")
