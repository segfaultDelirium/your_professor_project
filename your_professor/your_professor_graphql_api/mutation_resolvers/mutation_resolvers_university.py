from ..models import City, University
from ..mutation_payloads import create_mutation_payload, \
    create_mutation_payload_university
from neomodel import db


def resolve_create_university(_, info, local_language_name: str,
                              name: str = None, is_active: bool = None, founding_year: int = None, uid_city: str = None):
    try:
        probe = University.nodes.get(local_language_name=local_language_name)
        return create_mutation_payload_university(False,
                                                  "University of this local language name already exist.",
                                                  university=probe)
    except University.DoesNotExist as e:
        pass
    try:
        city_to_connect = City.nodes.get(uid=uid_city)
        new_university = University(local_language_name=local_language_name, name=name,
                                    is_active = is_active, founding_year = founding_year).save()
        new_university.city.connect(city_to_connect)
        new_university.save()
        return create_mutation_payload_university(True, university=new_university)
    except City.DoesNotExist as e:
        print(e)
        return create_mutation_payload(False, error=f"City of uid {uid_city} could not be found.")
    except Exception as e:
        print(e)
        return create_mutation_payload(False, error="Sum ting wong")


def resolve_update_university(_, info, uid, local_language_name=None, name=None, is_active=None,
                              founding_year: int = None, uid_city: str=None):
    try:
        university = University.nodes.get(uid=uid)
        if local_language_name is not None and local_language_name != "":
            university.local_language_name = local_language_name
        if name is not None and name != "":
            university.name = name
        if is_active is not None:
            university.is_active = is_active
        if founding_year is not None:
            university.founding_year = founding_year
        university.save()
        if uid_city is not None:
            city = City.nodes.get(uid=uid_city)
            old_city = university.city.all()[0]
            if old_city is None:
                university.city.connect(new_node=city)
                university.save()
            elif old_city.uid == city.uid:
                pass
            else:
                university.city.reconnect(old_node=old_city, new_node=city)
                university.save()
        return create_mutation_payload_university(True, university=university)
    except University.DoesNotExist:
        return create_mutation_payload(False, error=f"City of uid {uid} could not be found.")
    except City.DoesNotExist:
        return create_mutation_payload(False, error=f"Region of uid {uid_city} could not be found.")


def resolve_delete_university(_, info, uid: str, force: bool = False):
    try:
        city = City.nodes.get(uid=uid)
        if not force and len(city.universities.all()) != 0:
            return create_mutation_payload(False,
                                           "City you are trying to delete has Universities attached, "
                                           "please disconnect them before deleting it.")
        city.delete()
        return create_mutation_payload(True)
    except City.DoesNotExist:
        return create_mutation_payload(False, "City you are trying to delete does not exist")

