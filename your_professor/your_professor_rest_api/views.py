from django.shortcuts import render
from django.http import HttpResponse
from .models import (Person, Country, Region, City,
    University, Faculty, Specialization, ScienceDomain, Course)

# Create your views here.


def index(request):




    # print(poland)
    # print(poland.get_ISO_code_name_display())
    # poland.save()
    # jim = Person(name="Jim", age=34).save()  # Create
    # jim.age = 4
    # jim.save()
    # print(jim.uid)
    return HttpResponse("hello world")
