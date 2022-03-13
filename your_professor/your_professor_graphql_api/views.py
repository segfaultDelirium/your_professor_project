import datetime

from django.http import HttpResponse
from .models import (Country, Region, City,
    University, Faculty, Specialization, ScienceDomain, Course, Professor, ProfessorCourse, User)
from hashlib import pbkdf2_hmac
from os import urandom

# Create your views here.
#
# from .models import Book
#
# def get_books(request):
#     return render('')


def add_user():
    salt = urandom(32)
    password = "abandonship"
    password_hashed = pbkdf2_hmac('sha256', password.encode('UTF-8'), salt, 100000)
    user = User(username="Charlie", salt=salt.hex(), password=password_hashed, email="Charlie@gmail.com",
                first_name="Charlie", last_name="Charliee", birthday=datetime.datetime(2001, 3, 17))
    user.save()

    # verify:
    print(user.password)
    print(pbkdf2_hmac(
        'sha256',
        password.encode('UTF-8'),
        bytes.fromhex(user.salt),
        100000))


def index(request):

    return HttpResponse("hello world")
