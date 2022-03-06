from ..models import Region, Country, City
from ..mutation_payloads import create_mutation_payload_city, create_mutation_payload
from neomodel import db


def resolve_city(obj, info, uid=None):
    if obj is not None:
        return obj.cities.all()[0]
    try:
        return City.nodes.get(uid=uid)
    except City.DoesNotExist:
        return None


def resolve_all_cities(obj, info, amount: int = None):
    if obj is not None:
        if amount is None or amount >= len(City.nodes):
            return obj.cities.all()
        return obj.cities.all()[:amount]
    if amount is None or amount >= len(City.nodes):
        return City.nodes.all()
    return City.nodes.all()[:amount]


def resolve_create_city(_, info, local_language_name: str, name: str, uid_region: str):
    try:
        probing_city = City.nodes.get(local_language_name=local_language_name)
        return create_mutation_payload_city(False,
                                            "City of this local language name already exist.",
                                            city=probing_city)
    except City.DoesNotExist as e:
        pass
    try:
        region_to_connect = Region.nodes.get(uid=uid_region)
        new_city = City(local_language_name=local_language_name, name=name).save()
        new_city.region.connect(region_to_connect)
        new_city.save()
        return create_mutation_payload_city(True, city=new_city)
    except Region.DoesNotExist as e:
        print(e)
        return create_mutation_payload(False, error=f"Region of uid {uid_region} could not be found.")
    except Exception as e:
        print(e)
        return create_mutation_payload(False, error="Sum ting wong")


def resolve_update_city(_, info, uid, local_language_name=None, name=None, is_active=None, uid_region: str=None):
    try:
        city = City.nodes.get(uid=uid)
        if local_language_name is not None and local_language_name != "":
            city.local_language_name = local_language_name
        if name is not None and name != "":
            city.name = name
        if is_active is not None:
            city.is_active = is_active
        city.save()
        region = Region.nodes.get(uid=uid_region)
        old_region = city.region.all()[0]
        if old_region is None:
            city.region.connect(new_node=region)
            city.save()
        elif old_region.uid == region.uid:
            pass
        else:
            city.region.reconnect(old_node=old_region, new_node=region)
            city.save()
        return create_mutation_payload_city(True, city=city)
    except City.DoesNotExist:
        return create_mutation_payload(False, error=f"City of uid {uid} could not be found.")
    except Region.DoesNotExist:
        return create_mutation_payload(False, error=f"Region of uid {uid_region} could not be found.")


def resolve_delete_city(_, info, uid: str, force: bool = False):
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