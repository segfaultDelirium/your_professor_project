from ..models import Specialization, Course
from ..mutation_payloads import create_mutation_payload, \
    create_mutation_payload_course
from .resolver_utils import get_amount_or_all_of, get_nodes_by_uid_or_none_of


def resolve_course(obj, info, uid=None):
    if obj is not None:
        return obj.course.all()[0]
    return get_nodes_by_uid_or_none_of(Course, uid)


def resolve_all_courses(obj, info, amount: int = None):
    if obj is not None:
        if amount is None or amount >= len(obj.courses):
            return obj.courses.all()
        return obj.courses.all()[:amount]
    return get_amount_or_all_of(Course, amount)


def resolve_create_course(_, info, name: str, is_active: bool = None, lecture_hours_amount: int = None,
                          exercises_hours_amount: int = None, has_exam: bool = None, ECTS: int = None,
                          is_obligatory: bool = None, semester: int = None, uid_specialization: str = None):
    try:
        course_probe = Course.nodes.get(name=name)
        return create_mutation_payload_course(False,
                                                      "Course of this name already exist.",
                                                      course=course_probe)
    except Course.DoesNotExist as e:
        pass
    try:
        specialization_to_connect = Specialization.nodes.get(uid=uid_specialization)
        new_course = Course(name=name, is_active=is_active, lecture_hours_amount=lecture_hours_amount,
                            exercises_hours_amount=exercises_hours_amount, has_exam=has_exam, ECTS=ECTS,
                            is_obligatory=is_obligatory, semester=semester).save()
        new_course.specialization.connect(specialization_to_connect)
        new_course.save()
        return create_mutation_payload_course(True, course=new_course)
    except Specialization.DoesNotExist as e:
        print(e)
        return create_mutation_payload(False, error=f"Specialization of uid {uid_specialization} could not be found.")
    except Exception as e:
        print(e)
        return create_mutation_payload(False, error="Sum ting wong")


def resolve_update_course(_, info, uid, name: str, is_active: bool = None, lecture_hours_amount: int = None,
                          exercises_hours_amount: int = None, has_exam: bool = None, ECTS: int = None,
                          is_obligatory: bool = None, semester: int = None, uid_specialization: str = None):
    try:
        course = Course.nodes.get(uid=uid)
        if name is not None and name != "":
            course.name = name
        if is_active is not None:
            course.is_active = is_active
        if lecture_hours_amount is not None:
            course.lecture_hours_amount = lecture_hours_amount
        if exercises_hours_amount is not None:
            course.exercises_hours_amount = exercises_hours_amount
        if has_exam is not None:
            course.has_exam = has_exam
        if ECTS is not None:
            course.ECTS = ECTS
        if is_obligatory is not None:
            course.is_obligatory = is_obligatory
        if semester is not None:
            course.semester = semester
        course.save()
        # TODO take into consideration that course can belong to many specializations
        if uid_specialization is not None:
            specialization = Specialization.nodes.get(uid=uid_specialization)
            old_specialization = course.specialization.all()[0]
            if old_specialization is None:
                course.specialization.connect(new_node=specialization)
                course.save()
            elif old_specialization.uid == specialization.uid:
                pass
            else:
                course.specialization.reconnect(old_node=old_specialization, new_node=specialization)
                course.save()
        return create_mutation_payload_course(True, course=course)
    except Course.DoesNotExist:
        return create_mutation_payload(False, error=f"Course of uid {uid} could not be found.")
    except Specialization.DoesNotExist:
        return create_mutation_payload(False, error=f"Specialization of uid {uid_specialization} could not be found.")


def resolve_delete_course(_, info, uid: str, force: bool = False):
    try:
        course = Course.nodes.get(uid=uid)
        if not force and len(course.professor_course.all()) != 0:
            return create_mutation_payload(False,
                                           "Course you are trying to delete has Professors attached, "
                                           "please disconnect them before deleting it.")
        course.delete()
        return create_mutation_payload(True)
    except Course.DoesNotExist:
        return create_mutation_payload(False, "Course you are trying to delete does not exist")
