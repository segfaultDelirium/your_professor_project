from ..models import ScienceDomain, Specialization
from ..mutation_payloads import create_mutation_payload, \
    create_mutation_payload_specialization, create_mutation_payload_science_domain
from .resolver_utils import get_amount_or_all_of, get_nodes_by_uid_or_none_of


def resolve_science_domain(obj, info, uid=None):
    if obj is not None:
        return obj.specialization.all()[0]
    return get_nodes_by_uid_or_none_of(ScienceDomain, uid)


def resolve_all_science_domains(obj, info, amount: int = None):
    if obj is not None:
        if amount is None or amount >= len(obj.science_domains):
            return obj.science_domains.all()
        return obj.science_domains.all()[:amount]
    return get_amount_or_all_of(ScienceDomain, amount)

def resolve_create_science_domain(_, info, name: str, name_in_polish: str, is_active: bool = None):
    try:
        science_domain_probe = ScienceDomain.nodes.get(name=name)
        return create_mutation_payload_science_domain(False,
                                                      "ScienceDomain of this name already exist.",
                                                      science_domain=science_domain_probe)
    except ScienceDomain.DoesNotExist as e:
        pass
    try:
        science_domain = ScienceDomain(name=name, is_active=is_active, name_in_polish=name_in_polish).save()
        science_domain.save()
        return create_mutation_payload_science_domain(True, science_domain=science_domain)
    except Exception as e:
        print(e)
        return create_mutation_payload(False, error="Sum ting wong")


def resolve_update_science_domain(_, info, uid,name: str = None, name_in_polish: str = None, is_active: bool = None):
    try:
        science_domain = ScienceDomain.nodes.get(uid=uid)
        if name is not None and name != "":
            science_domain.name = name
        if is_active is not None:
            science_domain.is_active = is_active
        if name_in_polish is not None:
            science_domain.name_in_polish = name_in_polish
        science_domain.save()
        return create_mutation_payload_science_domain(True, science_domain=science_domain)
    except ScienceDomain.DoesNotExist:
        return create_mutation_payload(False, error=f"ScienceDomain of uid {uid} could not be found.")


def resolve_connect_science_domain_to_specialization(_, info, uid: str, uid_specialization: str):
    try:
        science_domain = ScienceDomain.nodes.get(uid=uid)
        specialization = Specialization.nodes.get(uid=uid_specialization)
        science_domain.specializations.connect(specialization)
        science_domain.save()
        return create_mutation_payload_science_domain(True, science_domain=science_domain)
    except ScienceDomain.DoesNotExist:
        return create_mutation_payload(False, error=f"ScienceDomain of uid {uid} could not be found.")
    except Specialization.DoesNotExist:
        return create_mutation_payload(False, error=f"Specialization of uid {uid_specialization} could not be found.")


def resolve_disconnect_science_domain_from_specialization(_, info, uid: str, uid_specialization: str):
    try:
        science_domain = ScienceDomain.nodes.get(uid=uid)
        specialization = Specialization.nodes.get(uid=uid_specialization)
        science_domain.specializations.disconnect(specialization)
        science_domain.save()
        return create_mutation_payload_science_domain(True, science_domain=science_domain)
    except ScienceDomain.DoesNotExist:
        return create_mutation_payload(False, error=f"ScienceDomain of uid {uid} could not be found.")
    except Specialization.DoesNotExist:
        return create_mutation_payload(False, error=f"Specialization of uid {uid_specialization} could not be found.")


def resolve_delete_science_domain(_, info, uid: str, force: bool = False):
    try:
        science_domain = ScienceDomain.nodes.get(uid=uid)
        if not force and len(science_domain.specializations) != 0:
            return create_mutation_payload(False,
                                           "ScienceDomain you are trying to delete has Specializations attached, "
                                           "please disconnect them before deleting it.")
        science_domain.delete()
        return create_mutation_payload(True)
    except Specialization.DoesNotExist:
        return create_mutation_payload(False, "Specialization you are trying to delete does not exist")
