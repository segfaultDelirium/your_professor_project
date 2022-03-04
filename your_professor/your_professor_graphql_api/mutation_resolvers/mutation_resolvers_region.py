from ..models import Region, Country
from ..mutation_payloads import create_mutation_payload_region, create_mutation_payload

def resolve_update_region(_, info, uid, local_language_name=None, name=None, is_active=None):
    print(uid)
    try:
        this_region = Region.nodes.get(uid=uid)
        if local_language_name is None or local_language_name == "":
            this_region.local_language_name = local_language_name
        if name is None or name == "": this_region.name = name
        if is_active is None: this_region.is_active = is_active
        this_region.save()
    except Region.DoesNotExist:
        return False

    return True


def resolve_reconnect_region_to_country(_, info, uid, country_uid):
    try:
        this_region = Region.nodes.get(uid=uid)
        this_country = Country.nodes.get(uid=country_uid)
        if this_country != this_region.country.all()[0]:
            this_region.country.reconnect(this_region.country.all()[0], this_country)
    except Region.DoesNotExist:
        return create_mutation_payload(False, f"Region of {uid=} does not exist.")
    this_region.save()
    return create_mutation_payload_region(True, region=this_region)


def resolve_create_region(_, info, local_language_name: str, name: str, uid_country: str):
    try:
        probing_region = Region.nodes.get(local_language_name=local_language_name)
        return create_mutation_payload_region(False,
                                              "Region of this local language name already exist.",
                                              region=probing_region)
    except Region.DoesNotExist as e:
        pass
    try:
        new_region = Region(local_language_name=local_language_name, name=name).save()
        country_to_connect = Country.nodes.get(uid=uid_country)
        new_region.country.connect(country_to_connect)
        new_region.save()
        create_mutation_payload_region(True, region=new_region)
    except Country.DoesNotExist as e:
        print(e)
        create_mutation_payload(False, error=f"Country of uid {uid_country} could not be found.")
    except Exception as e:
        print(e)
        create_mutation_payload(False, error = "Sum ting Wong")