from ..models import User, Professor, Course, Specialization
from ..mutation_payloads import create_mutation_payload, \
    create_mutation_payload_user
from .resolver_utils import (get_amount_or_all_of, get_nodes_by_uid_or_none_of, check_database_connection,
                             check_birthday_format)
from hashlib import pbkdf2_hmac
from os import urandom
from datetime import datetime
from ..constants import LOGIN_TIMESTAMP_FORMAT


@check_database_connection
def resolve_user(obj, info, uid=None):
    if obj is not None:
        return obj.user.all()[0]
    return get_nodes_by_uid_or_none_of(User, uid)


@check_database_connection
def resolve_all_users(obj, info, amount: int = None):
    if obj is not None:
        if amount is None or amount >= len(obj.users):
            return obj.users.all()
        return obj.users.all()[:amount]
    return get_amount_or_all_of(User, amount)


@check_database_connection
def resolve_create_user(_, info, is_active: bool = None, username: str = None, password: str = None,
                        email_address: str = None, is_staff: bool = None, is_super_user: bool = None,
                        first_name: str = None, last_name: str = None, birthday: str = None, is_male: bool = None):
    try:
        User.nodes.get(username=username)
        return create_mutation_payload(False, error="user of this username already exists")
    except User.DoesNotExist:
        pass
    birthday_checked = check_birthday_format(birthday)
    if not birthday_checked["status"]: return birthday_checked["error"]
    birthday = birthday_checked["birthday"]
    try:
        salt = urandom(32)
        password_hashed = pbkdf2_hmac('sha256', password.encode('UTF-8'), salt, 100000)
        user = User(is_active=is_active, username=username, salt=salt.hex(), password=password_hashed,
                    email_address=email_address, is_staff=is_staff, is_super_user=is_super_user,
                    first_name=first_name, last_name=last_name, birthday=birthday, is_male=is_male).save()
        return create_mutation_payload_user(True, user=user)
    except Exception as e:
        print(e)
        return create_mutation_payload(False, error="Sum ting wong")


def resolve_update_most_recent_login_timestamp_user(_, info, uid, most_recent_login_timestamp: str):
    try:
        user = User.nodes.get(uid=uid)
        user.most_recent_login_timestamp = datetime.strptime(most_recent_login_timestamp, LOGIN_TIMESTAMP_FORMAT)
        return create_mutation_payload_user(True, user=user)
    except User.DoesNotExist:
        return create_mutation_payload(False, f"user of {uid=} does not exist")
    except ValueError:
        return create_mutation_payload(False, f"most_recent_login_timestamp is of incorrect format,"
                                              f" correct fromat: {LOGIN_TIMESTAMP_FORMAT}")


@check_database_connection
def resolve_update_user(_, info, uid: str, is_active: bool = None, username: str = None, password: str = None,
                             email_address: str = None, is_staff: bool = None, is_super_user: bool = None,
                             first_name: str = None, last_name: str = None, birthday: datetime = None,
                             is_male: bool = None):
    birthday_checked = check_birthday_format(birthday)
    if not birthday_checked["status"]:
        return birthday_checked["error"]
    birthday = birthday_checked["birthday"]
    user = None
    try:
        user = User.nodes.get(uid=uid)
    except User.DoesNotExist:
        return create_mutation_payload(False, error=f"User of uid {uid} could not be found.")
    if username is not None:
        try:
            user = User.nodes.get(username=username)
            return create_mutation_payload(False, error=f"User of {username=} already exists, cannot change your"
                                                        " current username to new one.")
        except User.DoesNotExist:
            user.username = username
    try:
        if is_active is not None: user.is_active = is_active
        if password is not None:
            user.password = pbkdf2_hmac('sha256', password.encode('UTF-8'), bytes.fromhex(user.salt), 100000)
        if email_address is not None: user.email_address = email_address
        if is_staff is not None: user.is_staff = is_staff
        if is_super_user is not None: user.is_super_user = is_super_user
        if first_name is not None: user.first_name = first_name
        if last_name is not None: user.last_name = last_name
        if birthday is not None: user.birth_year = birthday
        if is_male is not None: user.is_male = is_male
        user.save()
        return create_mutation_payload_user(True, user=user)
    except Exception as e:
        print(e)
        return create_mutation_payload(False, error="Sum ting wong")


def resolve_connect_user_to_specialization(_, info, uid: str, uid_specialization: str):
    try:
        user = User.nodes.get(uid=uid)
        specialization = Specialization.nodes.get(uid=uid_specialization)
        user.specialization.connect(specialization)
        user.save()
        return create_mutation_payload_user(True, user=user)
    except User.DoesNotExist:
        return create_mutation_payload(False, error=f"User of {uid=} could not be found.")
    except Specialization.DoesNotExist:
        return create_mutation_payload(False, error=f"Specialization of {uid_specialization=} could not be found.")


def resolve_disconnect_user_from_specialization(_, info, uid: str, uid_specialization: str):
    try:
        user = User.nodes.get(uid=uid)
        specialization = Specialization.nodes.get(uid=uid_specialization)
        user.specialization.disconnect(specialization)
        user.save()
        return create_mutation_payload_user(True, user=user)
    except User.DoesNotExist:
        return create_mutation_payload(False, error=f"User of {uid=} could not be found.")
    except Specialization.DoesNotExist:
        return create_mutation_payload(False, error=f"Specialization of {uid_specialization=} could not be found.")


def resolve_connect_user_to_course(_, info, uid: str, uid_course: str):
    try:
        user = User.nodes.get(uid=uid)
        course = Course.nodes.get(uid=uid_course)
        user.course.connect(course)
        user.save()
        return create_mutation_payload_user(True, user=user)
    except User.DoesNotExist:
        return create_mutation_payload(False, error=f"User of {uid=} could not be found.")
    except Course.DoesNotExist:
        return create_mutation_payload(False, error=f"Course of {uid_course=} could not be found.")


def resolve_disconnect_user_from_course(_, info, uid: str, uid_course: str):
    try:
        user = User.nodes.get(uid=uid)
        course = Course.nodes.get(uid=uid_course)
        user.course.disconnect(course)
        user.save()
        return create_mutation_payload_user(True, user=user)
    except User.DoesNotExist:
        return create_mutation_payload(False, error=f"User of {uid=} could not be found.")
    except Course.DoesNotExist:
        return create_mutation_payload(False, error=f"Course of {uid_course=} could not be found.")


@check_database_connection
def resolve_delete_user(_, info, uid: str, force: bool = False):
    try:
        user = User.nodes.get(uid=uid)
        # if not force and len(user.professor_courses.all()) != 0:
        #     return create_mutation_payload(False,
        #                                    "Professor you are trying to delete has Courses attached, "
        #                                    "please disconnect them before deleting it.")
        user.delete()
        return create_mutation_payload(True)
    except User.DoesNotExist:
        return create_mutation_payload(False, "Professor you are trying to delete does not exist")
