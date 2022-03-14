from ..models import University, Faculty
from ..mutation_payloads import create_mutation_payload, \
    create_mutation_payload_faculty
from .resolver_utils import get_amount_or_all_of, get_nodes_by_uid_or_none_of


def resolve_faculty(obj, info, uid=None):
    if obj is not None:
        return obj.faculty.all()[0]
    return get_nodes_by_uid_or_none_of(Faculty, uid)


def resolve_all_faculties(obj, info, amount: int = None):
    if obj is not None:
        if amount is None or amount >= len(obj.faculties):
            return obj.faculties.all()
        return obj.faculties.all()[:amount]
    return get_amount_or_all_of(Faculty, amount)


def resolve_create_faculty(_, info, name: str = None, is_active: bool = None, uid_university: str = None):
    try:
        faculty_probe = Faculty.nodes.get(name=name)
        return create_mutation_payload_faculty(False,
                                                  "Faculty of this name already exist.",
                                                  faculty=faculty_probe)
    except Faculty.DoesNotExist as e:
        pass
    try:
        faculty_to_connect = University.nodes.get(uid=uid_university)
        new_faculty = Faculty(name=name, is_active = is_active,).save()
        new_faculty.university.connect(faculty_to_connect)
        new_faculty.save()
        return create_mutation_payload_faculty(True, faculty=new_faculty)
    except University.DoesNotExist as e:
        print(e)
        return create_mutation_payload(False, error=f"University of uid {uid_university} could not be found.")
    except Exception as e:
        print(e)
        return create_mutation_payload(False, error="Sum ting wong")


def resolve_update_faculty(_, info, uid, name=None, is_active=None, uid_university: str=None):
    try:
        faculty = Faculty.nodes.get(uid=uid)
        if name is not None and name != "":
            faculty.name = name
        if is_active is not None:
            faculty.is_active = is_active
        faculty.save()
        if uid_university is not None:
            university = University.nodes.get(uid=uid_university)
            old_university = faculty.university.all()[0]
            if old_university is None:
                faculty.university.connect(new_node=university)
                faculty.save()
            elif old_university.uid == university.uid:
                pass
            else:
                faculty.university.reconnect(old_node=old_university, new_node=university)
                faculty.save()
        return create_mutation_payload_faculty(True, faculty=faculty)
    except Faculty.DoesNotExist:
        return create_mutation_payload(False, error=f"University of uid {uid} could not be found.")
    except University.DoesNotExist:
        return create_mutation_payload(False, error=f"Region of uid {uid_university} could not be found.")


def resolve_delete_faculty(_, info, uid: str, force: bool = False):
    try:
        faculty = Faculty.nodes.get(uid=uid)
        if not force and len(faculty.specializations.all()) != 0:
            return create_mutation_payload(False,
                                           "Faculty you are trying to delete has Specializations attached, "
                                           "please disconnect them before deleting it.")
        faculty.delete()
        return create_mutation_payload(True)
    except Faculty.DoesNotExist:
        return create_mutation_payload(False, "Faculty you are trying to delete does not exist")

