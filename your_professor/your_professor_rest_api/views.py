from django.shortcuts import render
from django.http import HttpResponse
from .models import Person, Country

# Create your views here.


def index(request):
    # jim = Person(name="Jim", age=34).save()  # Create
    # jim.age = 4
    # jim.save()
    # print(jim.uid)
    return HttpResponse("hello world")

