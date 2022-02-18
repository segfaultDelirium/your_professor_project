import datetime

from django.http import HttpResponse
from .models import (Person, Country, Region, City,
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
    print(Country.nodes.all())
    user = User.nodes.get(last_name="Charliee")
    print(user.date_joined)

    # gawron = Professor(first_name="Przemysław", last_name="Gawroński", is_male=True, degree='3').save()
    # beata = Professor(first_name="Beata", last_name="Orchel", is_male=False, degree='3').save()

    # beata = Professor.nodes.get(uid="04a5037c69974419b3f6cc637c833941")
    #
    # # pc = ProfessorCourse.nodes.get(uid="e5822502e5cc4a52b5e7e97ba298956e")
    # pc = ProfessorCourse(is_professor_lecturer=True).save()
    # pc.course.connect(Course.nodes.get(uid="762b7c41476d415582dd00ef729d2d36"))
    # pc.professor.connect(beata)

    # pc = ProfessorCourse(is_professor_lecturer=True).save()
    # pc.course.connect()
    # pc.professor.connect(Professor.nodes.get(uid="1255b63f76ff4c98bf5f456f707da6be"))


    # algorytmy_pc = ProfessorCourse.nodes.get(uid="e5822502e5cc4a52b5e7e97ba298956e")
    # algorytmy_pc.professor.connect(Professor.nodes.get(uid="1255b63f76ff4c98bf5f456f707da6be"))
    # print(Professor.nodes.get(uid="1255b63f76ff4c98bf5f456f707da6be"))

    # print(poland)
    # print(poland.get_ISO_code_name_display())
    # poland.save()
    # jim = Person(name="Jim", age=34).save()  # Create
    # jim.age = 4
    # jim.save()
    # print(jim.uid)
    return HttpResponse("hello world")
