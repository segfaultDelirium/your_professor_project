from ..models import Country, COUNTRIES
from ..mutation_payloads import create_mutation_payload_country, create_mutation_payload


def resolve_create_country_by_ISO(_, info, local_language_name: str, ISO_code_name: str):
    if COUNTRIES.get(ISO_code_name) is None:
        return create_mutation_payload(False, "Incorrect ISO code")
    print(COUNTRIES.get(ISO_code_name))
    try:
        probing_country = Country.nodes.get(ISO_code_name=ISO_code_name)
        return create_mutation_payload(False, "Country with this ISO code already exist")
    except Country.DoesNotExist as e:
        pass
    try:
        new_country = Country(local_language_name=local_language_name, ISO_code_name=ISO_code_name).save()
        create_mutation_payload_country(True, country=new_country)
    except Exception as e:
        print(e)
        create_mutation_payload(False, error="Sum ting Wong")


def resolve_update_country(_, info, uid: str, local_language_name: str, ISO_code_name: str, is_active: bool):
    print(uid)
    try:
        this_country = Country.nodes.get(uid=uid)
        if local_language_name is not None or local_language_name != "":
            this_country.local_language_name = local_language_name
        if ISO_code_name is not None and ISO_code_name != "":
            this_country.ISO_code_name = ISO_code_name
        if is_active is not None:
            this_country.is_active = is_active
        this_country.save()
    except Country.DoesNotExist:
        return create_mutation_payload(False, "Country you are trying to modify does not exist")
    return create_mutation_payload_country(True, country=this_country)


def resolve_delete_country(_, info, uid: str, force: bool = False):
    try:
        this_country = Country.nodes.get(uid=uid)
        if not force and len(this_country.regions.all()) != 0:
            return create_mutation_payload(False,
                                           "Country you are trying to delete has regions attached, "
                                           "please disconnect them before deleting Country.")
        this_country.delete()
        return create_mutation_payload(True)
    except Country.DoesNotExist:
        return create_mutation_payload(False, "Country you are trying to delete does not exist")
