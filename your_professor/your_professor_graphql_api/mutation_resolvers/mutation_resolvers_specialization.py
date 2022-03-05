from ..models import Faculty, Specialization
from ..mutation_payloads import create_mutation_payload, \
    create_mutation_payload_specialization


def resolve_create_specialization(_, info, name: str, is_active: bool = None, is_full_time: bool = None,
                                  specialization_degree: int = None, uid_faculty: str = None):
    try:
        specialization_probe = Specialization.nodes.get(name=name)
        return create_mutation_payload_specialization(False,
                                                      "Specialization of this name already exist.",
                                                      specialization=specialization_probe)
    except Specialization.DoesNotExist as e:
        pass
    try:
        faculty_to_connect = Faculty.nodes.get(uid=uid_faculty)
        new_specialization = Specialization(name=name, is_active=is_active, is_full_time=is_full_time,
                                            specialization_degree=specialization_degree).save()
        new_specialization.faculty.connect(faculty_to_connect)
        new_specialization.save()
        return create_mutation_payload_specialization(True, specialization=new_specialization)
    except Faculty.DoesNotExist as e:
        print(e)
        return create_mutation_payload(False, error=f"Faculty of uid {uid_faculty} could not be found.")
    except Exception as e:
        print(e)
        return create_mutation_payload(False, error="Sum ting wong")


def resolve_update_specialization(_, info, uid, name: str = None, is_active: bool = None, is_full_time: bool = None,
                                  specialization_degree: int = None, uid_faculty: str = None):
    try:
        specialization = Specialization.nodes.get(uid=uid)
        if name is not None and name != "":
            specialization.name = name
        if is_active is not None:
            specialization.is_active = is_active
        if is_full_time is not None:
            specialization.is_full_time = is_full_time
        if specialization_degree is not None:
            specialization.specialization_degree = specialization_degree
        specialization.save()
        if uid_faculty is not None:
            faculty = Faculty.nodes.get(uid=uid_faculty)
            old_faculty = specialization.faculty.all()[0]
            if old_faculty is None:
                specialization.faculty.connect(new_node=faculty)
                specialization.save()
            elif old_faculty.uid == faculty.uid:
                pass
            else:
                specialization.faculty.reconnect(old_node=old_faculty, new_node=faculty)
                specialization.save()
        return create_mutation_payload_specialization(True, specialization=specialization)
    except Specialization.DoesNotExist:
        return create_mutation_payload(False, error=f"Faculty of uid {uid} could not be found.")
    except Faculty.DoesNotExist:
        return create_mutation_payload(False, error=f"Faculty of uid {uid_faculty} could not be found.")


def resolve_delete_specialization(_, info, uid: str, force: bool = False):
    try:
        specialization = Specialization.nodes.get(uid=uid)
        if not force and len(specialization.courses.all()) != 0:
            return create_mutation_payload(False,
                                           "Specialization you are trying to delete has Specializations attached, "
                                           "please disconnect them before deleting it.")
        specialization.delete()
        return create_mutation_payload(True)
    except Specialization.DoesNotExist:
        return create_mutation_payload(False, "Specialization you are trying to delete does not exist")
