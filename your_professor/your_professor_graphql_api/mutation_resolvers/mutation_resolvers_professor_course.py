from ..models import Course, ProfessorCourse, Professor
from ..mutation_payloads import create_mutation_payload, \
    create_mutation_payload_professor_course


def resolve_create_professor_course(_, info, is_active: bool = None, uid_course: str = None, uid_professor: str = None,
                                    is_professor_lecturer: bool = None):
    try:
        course_to_connect = Course.nodes.get(uid=uid_course)
        professor_to_connect = None
        if uid_professor is not None:
            professor_to_connect = Professor.nodes.get(uid = uid_professor)
        new_professor_course = ProfessorCourse(is_active=is_active,
                                               is_professor_lecturer=is_professor_lecturer).save()
        new_professor_course.course.connect(course_to_connect)
        if professor_to_connect is not None:
            new_professor_course.professor.connect(professor_to_connect)
        new_professor_course.save()
        return create_mutation_payload_professor_course(True, professor_course=new_professor_course)
    except Course.DoesNotExist as e:
        print(e)
        return create_mutation_payload(False, error=f"Course of uid {uid_course} could not be found.")
    except Professor.DoesNotExist as e:
        print(e)
        return create_mutation_payload(False, error=f"Professor of uid {uid_professor} could not be found.")
    except Exception as e:
        print(e)
        return create_mutation_payload(False, error="Sum ting wong")


def resolve_update_professor_course(_, info, uid, is_active: bool = None, uid_course: str = None, uid_professor: str = None,
                                    is_professor_lecturer: bool = None):
    try:
        professor_course = ProfessorCourse.nodes.get(uid=uid)
        if is_active is not None:
            professor_course.is_active = is_active
        if is_professor_lecturer is not None:
            professor_course.is_professor_lecturer = is_professor_lecturer
        professor_course.save()
        if uid_course is not None:
            course = Course.nodes.get(uid=uid_course)
            old_course = professor_course.course.all()[0]
            if old_course is None:
                professor_course.course.connect(new_node=course)
                professor_course.save()
            elif old_course.uid == course.uid:
                pass
            else:
                professor_course.course.reconnect(old_node=old_course, new_node=course)
                professor_course.save()
        if uid_professor is not None:
            professor = Professor.nodes.get(uid=uid_professor)
            old_professor = professor_course.professor.all()[0]
            if old_professor is None:
                professor_course.professor.connect(new_node=professor)
                professor_course.save()
            elif old_professor.uid == professor.uid:
                pass
            else:
                professor_course.professor.reconnect(old_node=old_professor, new_node=professor)
                professor_course.save()
        return create_mutation_payload_professor_course(True, professor_course=professor_course)
    except ProfessorCourse.DoesNotExist:
        return create_mutation_payload(False, error=f"ProfessorCourse of uid {uid} could not be found.")
    except Course.DoesNotExist:
        return create_mutation_payload(False, error=f"Course of uid {uid_course} could not be found.")


def resolve_delete_professor_course(_, info, uid: str, force: bool = False):
    try:
        professor_course = ProfessorCourse.nodes.get(uid=uid)
        if not force and len(professor_course.professor.all()) != 0:
            return create_mutation_payload(False,
                                           "ProfessorCourse you are trying to delete has Professor attached, "
                                           "please disconnect it before deleting it.")
        professor_course.delete()
        return create_mutation_payload(True)
    except ProfessorCourse.DoesNotExist:
        return create_mutation_payload(False, "ProfessorCourse you are trying to delete does not exist")
