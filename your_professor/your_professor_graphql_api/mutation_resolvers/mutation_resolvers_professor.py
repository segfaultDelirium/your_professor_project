from ..models import ProfessorCourse, Professor
from ..mutation_payloads import create_mutation_payload, \
    create_mutation_payload_professor


def resolve_create_professor(_, info, first_name: str, last_name: str, is_active: bool = None, birth_year: int = None,
                             is_male: bool = None, degree: str = None, uid_professor_course: str = None):
    try:
        professor_course_to_connect = ProfessorCourse.nodes.get(uid=uid_professor_course)
        new_professor = Professor(first_name=first_name, last_name=last_name, is_active=is_active,
                                  birth_year=birth_year, is_male=is_male, degree=degree).save()
        new_professor.professor_course.connect(professor_course_to_connect)
        new_professor.save()
        return create_mutation_payload_professor(True, professor=new_professor)
    except ProfessorCourse.DoesNotExist as e:
        print(e)
        return create_mutation_payload(False,
                                       error=f"ProfessorCourse of uid {uid_professor_course} could not be found.")
    except Exception as e:
        print(e)
        return create_mutation_payload(False, error="Sum ting wong")


def resolve_update_professor(_, info, uid: str, first_name: str = None, last_name: str = None, is_active: bool = None,
                             birth_year: int = None, is_male: bool = None, degree: str = None,
                             uid_professor_course: str = None):
    try:
        professor = Professor.nodes.get(uid=uid)
        if first_name is not None and first_name != "":
            professor.name = first_name
        if last_name is not None and last_name != "":
            professor.name = last_name
        if is_active is not None:
            professor.is_active = is_active
        if birth_year is not None:
            professor.birth_year = birth_year
        if is_male is not None:
            professor.is_male = is_male
        if degree is not None:
            professor.degree = degree
        professor.save()
        if uid_professor_course is not None:
            professor_course = ProfessorCourse.nodes.get(uid=uid_professor_course)
            old_professor_course = professor.professor_course.all()[0]
            if old_professor_course is None:
                professor.professor_course.connect(new_node=professor_course)
                professor.save()
            elif old_professor_course.uid == professor_course.uid:
                pass
            else:
                professor.professor_course.reconnect(old_node=old_professor_course, new_node=professor_course)
                professor.save()
        return create_mutation_payload_course(True, professor=course)
    except Professor.DoesNotExist:
        return create_mutation_payload(False, error=f"Professor of uid {uid} could not be found.")
    except ProfessorCourse.DoesNotExist:
        return create_mutation_payload(False,
                                       error=f"ProfessorCourse of uid {uid_professor_course} could not be found.")


def resolve_delete_professor(_, info, uid: str, force: bool = False):
    try:
        professor = Professor.nodes.get(uid=uid)
        if not force and len(course.professor_course.all()) != 0:
            return create_mutation_payload(False,
                                           "Professor you are trying to delete has Professors attached, "
                                           "please disconnect them before deleting it.")
        professor.delete()
        return create_mutation_payload(True)
    except Professor.DoesNotExist:
        return create_mutation_payload(False, "Professor you are trying to delete does not exist")
