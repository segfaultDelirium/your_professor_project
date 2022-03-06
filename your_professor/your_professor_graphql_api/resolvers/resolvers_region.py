from ..models import Region, Country
from ..mutation_payloads import create_mutation_payload_region, create_mutation_payload
from neomodel.exceptions import AttemptedCardinalityViolation


def resolve_region(obj, info, uid):
    if obj is not None:
        return obj.country.all()[0]
    try:
        return Region.nodes.get(uid=uid)
    except Region.DoesNotExist:
        return None


def resolve_all_regions(_, info, amount: int = None):
    print("in resolve_all_regions, amount = ", amount)
    if amount is None or amount >= len(Region.nodes):
        return Region.nodes.all()
    return Region.nodes.all()[:amount]


def resolve_create_region(_, info, local_language_name: str, name: str, uid_country: str):
    try:
        probing_region = Region.nodes.get(local_language_name=local_language_name)
        return create_mutation_payload_region(False,
                                              "Region of this local language name already exist.",
                                              region=probing_region)
    except Region.DoesNotExist as e:
        pass
    try:
        country_to_connect = Country.nodes.get(uid=uid_country)
        new_region = Region(local_language_name=local_language_name, name=name).save()
        new_region.country.connect(country_to_connect)
        new_region.save()
        return create_mutation_payload_region(True, region=new_region)
    except Country.DoesNotExist as e:
        print(e)
        return create_mutation_payload(False, error=f"Country of uid {uid_country} could not be found.")
    except Exception as e:
        print(e)
        return create_mutation_payload(False, error="Sum ting Wong")


def resolve_update_region(_, info, uid, local_language_name=None, name=None, is_active=None, uid_country: str = None):
    try:
        region = Region.nodes.get(uid=uid)
        if local_language_name is not None and local_language_name != "":
            region.local_language_name = local_language_name
        if name is not None and name != "":
            region.name = name
        if is_active is not None:
            region.is_active = is_active
        region.save()
        country = Country.nodes.get(uid=uid_country)
        old_country = region.country.all()[0]
        if old_country is None:
            region.country.connect(new_node=country)
            region.save()
        elif country.uid == old_country.uid:
            pass
        else:
            region.country.reconnect(old_node=old_country, new_node=country)
            region.save()
        return create_mutation_payload_region(True, region=region)
    except Region.DoesNotExist:
        return create_mutation_payload(False, error=f"Region of uid {uid} could not be found.")
    except Country.DoesNotExist:
        return create_mutation_payload(False, error=f"Country of uid {uid} could not be found.")


def resolve_delete_region(_, info, uid: str, force: bool = False):
    try:
        this_region = Region.nodes.get(uid=uid)
        if not force and len(this_region.cities.all()) != 0:
            return create_mutation_payload(False,
                                           "Region you are trying to delete has cities attached, "
                                           "please disconnect them before deleting it.")
        this_region.delete()
        return create_mutation_payload(True)
    except Region.DoesNotExist:
        return create_mutation_payload(False, "Region you are trying to delete does not exist")
