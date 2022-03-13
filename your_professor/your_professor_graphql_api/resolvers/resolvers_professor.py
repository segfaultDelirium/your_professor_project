from ..models import Professor, Course, TeachesCourse
from ..mutation_payloads import create_mutation_payload, \
    create_mutation_payload_professor
from .resolver_utils import get_amount_or_all_of, get_nodes_by_uid_or_none_of
from neomodel import db

def resolve_professor(obj, info, uid=None):
    if obj is not None:
        print(obj.professor.all()[0])
        return obj.professor.all()[0]
    return get_nodes_by_uid_or_none_of(Professor, uid)


def resolve_all_professors(obj, info, amount: int = None):
    if obj is not None:
        if amount is None or amount >= len(obj.professors):
            return obj.professors.all()
        return obj.professors.all()[:amount]
    return get_amount_or_all_of(Professor, amount)


def resolve_professor_teaches(obj, info):
    results, meta = db.cypher_query(f'match(n:Professor)-[r]->(c:Course) where n.uid="{obj.uid}" return r')
    rels = [TeachesCourse.inflate(row[0]) for row in results]
    res = []
    for rel in rels:
        res.append({'is_active': rel.is_active, 'is_professor_lecturer': rel.is_professor_lecturer,
                    'course': rel.end_node()})
    return res


def resolve_create_professor(_, info, first_name: str, last_name: str, is_active: bool = None, birth_year: int = None,
                             is_male: bool = None, degree: str = None, professor_teaches_details_list: [] = None):
    db.begin()
    try:
        new_professor = Professor(first_name=first_name, last_name=last_name, is_active=is_active,
                                  birth_year=birth_year, is_male=is_male, degree=degree).save()
        if professor_teaches_details_list is not None and len(professor_teaches_details_list) != 0 :
            for professor_teaches_details in professor_teaches_details_list:
                try:
                    course = Course.nodes.get(uid=professor_teaches_details["uid_course"])
                    rel = new_professor.courses.connect(course)
                    rel.is_active = professor_teaches_details["is_active"]
                    rel.is_professor_lecturer = professor_teaches_details["is_professor_lecturer"]
                except Course.DoesNotExist as e:
                    db.rollback()
                    return create_mutation_payload(False,
                                                   error=f'Course of uid: '
                                                         f'{professor_teaches_details["uid_course"]}'
                                                         f'could not be found.')
        new_professor.save()
        db.commit()
        return create_mutation_payload_professor(True, professor=new_professor)
    except Exception as e:
        print(e)
        return create_mutation_payload(False, error="Sum ting wong")


def resolve_update_professor(_, info, uid: str, first_name: str = None, last_name: str = None, is_active: bool = None,
                             birth_year: int = None, is_male: bool = None, degree: str = None,
                             uid_professor_course: str = None):
    try:
        professor = Professor.nodes.get(uid=uid)
        if first_name is not None and first_name != "":
            professor.first_name = first_name
        if last_name is not None and last_name != "":
            professor.last_name = last_name
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
        return create_mutation_payload_professor(True, professor=professor)
    except Professor.DoesNotExist:
        return create_mutation_payload(False, error=f"Professor of uid {uid} could not be found.")
    except ProfessorCourse.DoesNotExist:
        return create_mutation_payload(False,
                                       error=f"ProfessorCourse of uid {uid_professor_course} could not be found.")


def resolve_connect_professor_to_professor_course(_, info, uid: str, uid_professor_course: str):
    try:
        professor = Professor.nodes.get(uid=uid)
        professor_course = ProfessorCourse.nodes.get(uid=uid_professor_course)
        professor.professor_course.connect(professor_course)
        professor.save()
        return create_mutation_payload_professor(True, professor=professor)
    except Professor.DoesNotExist:
        return create_mutation_payload(False, error=f"Professor of uid {uid} could not be found.")
    except ProfessorCourse.DoesNotExist:
        return create_mutation_payload(False,
                                       error=f"ProfessorCourse of uid {uid_professor_course} could not be found.")


def resolve_reconnect_professor_to_professor_course(_, info, uid: str, uid_old_professor_course: str,
                                                    uid_new_professor_course: str):
    old_professor_course = None
    try:
        old_professor_course = ProfessorCourse.nodes.get(uid=uid_old_professor_course)
    except ProfessorCourse.DoesNotExist:
        return create_mutation_payload(False,
                                       error=f"Old ProfessorCourse of uid {uid_old_professor_course} "
                                             "could not be found.")
    try:
        professor = Professor.nodes.get(uid=uid)
        new_professor_course = ProfessorCourse.nodes.get(uid=uid_new_professor_course)
        professor.professor_courses.reconnect(old_node=old_professor_course, new_node=new_professor_course)
        professor.save()
        return create_mutation_payload_professor(True, professor=professor)
    except Professor.DoesNotExist:
        return create_mutation_payload(False, error=f"Professor of uid {uid} could not be found.")
    except ProfessorCourse.DoesNotExist:
        return create_mutation_payload(False,
                                       error=f"New ProfessorCourse of uid {uid_old_professor_course} "
                                             "could not be found.")


def resolve_disconnect_professor_from_professor_course(_, info, uid: str, uid_professor_course: str):
    try:
        professor = Professor.nodes.get(uid=uid)
        professor_course = ProfessorCourse.nodes.get(uid=uid_professor_course)
        professor.professor_courses.disconnect(professor_course)
        professor.save()
        return create_mutation_payload_professor(True, professor=professor)
    except Professor.DoesNotExist:
        return create_mutation_payload(False, error=f"Professor of uid {uid} could not be found.")
    except ProfessorCourse.DoesNotExist:
        return create_mutation_payload(False,
                                       error=f"ProfessorCourse of uid {uid_professor_course} could not be found.")


def resolve_delete_professor(_, info, uid: str, force: bool = False):
    try:
        professor = Professor.nodes.get(uid=uid)
        if not force and len(professor.professor_courses.all()) != 0:
            return create_mutation_payload(False,
                                           "Professor you are trying to delete has Courses attached, "
                                           "please disconnect them before deleting it.")
        professor.delete()
        return create_mutation_payload(True)
    except Professor.DoesNotExist:
        return create_mutation_payload(False, "Professor you are trying to delete does not exist")
