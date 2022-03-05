from django.db import models
from .constants import DEGREES, COUNTRIES

# Create your models here.

from django_neomodel import DjangoNode
from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, RelationshipFrom, BooleanProperty,
                      EmailProperty, DateTimeProperty, DateProperty, Relationship, StructuredRel,
                      ZeroOrMore, One, ZeroOrOne, OneOrMore)


# TODO add cardinality to models
# TODO add relation properties similar to class ReactsTo(StructuredRel)



# class Book(StructuredNode):
#     title = StringProperty(unique_index=True)
#     published = DateProperty()
#

class Country(DjangoNode):
    uid = UniqueIdProperty()
    local_language_name = StringProperty(required=True)
    ISO_code_name = StringProperty(choices=COUNTRIES, required=True, unique_index=True)
    is_active = BooleanProperty(default=True)
    # language = StringProperty(max_length=100, required=True)
    regions = RelationshipTo("Region", "CONTAINS_REGION", cardinality=ZeroOrMore)


class Region(StructuredNode):  # example Malopolskie
    uid = UniqueIdProperty()
    local_language_name = StringProperty(max_length=100, required=True)
    name = StringProperty(max_length=100, required=False)  # region may not have english version of its name
    is_active = BooleanProperty(default=True)
    country = RelationshipFrom(Country, "CONTAINS_REGION", cardinality=One)
    cities = RelationshipTo("City", "CONTAINS CITY", cardinality=ZeroOrMore)


class City(StructuredNode):
    uid = UniqueIdProperty()
    local_language_name = StringProperty(required=True)
    name = StringProperty(max_length=100)
    is_active = BooleanProperty(default=True)
    region = RelationshipFrom(Region, "CONTAINS CITY", cardinality=One)
    universities = RelationshipTo("University", "HOSTS_UNIVERSITY", cardinality=ZeroOrMore)


class University(StructuredNode):  # example University of science and technology or Akademia Gorniczo Hutnicza
    uid = UniqueIdProperty()
    local_language_name = StringProperty(max_length=100, required=True)
    name = StringProperty(max_length=100)
    is_active = BooleanProperty(default=True)
    founding_year = IntegerProperty(required=False)
    city = RelationshipFrom(City, "HOSTS_UNIVERSITY", cardinality=One)
    review = RelationshipFrom('Review', "reviews", cardinality=ZeroOrMore)
    faculties = RelationshipTo("Faculty", "HAS_FACULTY", cardinality=ZeroOrMore)


class Faculty(StructuredNode):  # example "wydzial fizyki i informatyki stosowanej"
    uid = UniqueIdProperty()
    name = StringProperty(max_length=100)
    is_active = BooleanProperty(default=True)
    university = RelationshipFrom(University, "HAS_FACULTY", cardinality=One)
    review = RelationshipFrom('Review', "reviews", cardinality=ZeroOrMore)
    specializations = RelationshipTo("Specialization", "HAS_SPECIALIZATION", cardinality=ZeroOrMore)


class ScienceDomain(StructuredNode):  # example biology, computer science
    uid = UniqueIdProperty()
    name = StringProperty(max_length=100, required=True)
    name_in_polish = StringProperty()
    is_active = BooleanProperty(default=True)


class Specialization(StructuredNode):  # example "informatyka stosowana", "fizyka medyczna"
    uid = UniqueIdProperty()
    name = StringProperty(max_length=100)
    is_active = BooleanProperty(default=True)
    is_full_time = BooleanProperty(required=True)
    specialization_degree = IntegerProperty()  # 0 bachelor, 1 master, 2 doctor
    faculty = RelationshipFrom(Faculty, "HAS_SPECIALIZATION", cardinality=One)
    science_domains = RelationshipTo(ScienceDomain, "IS_PART_OF_DOMAIN", cardinality=ZeroOrMore)
    courses = RelationshipTo("Course", "HAS_COURSE", cardinality=ZeroOrMore)
    review = RelationshipFrom('Review', "reviews", cardinality=ZeroOrMore)


class Course(StructuredNode):  # example "Python in the enterprise" or "Bazy danych 1"
    uid = UniqueIdProperty()
    name = StringProperty(max_length=100)
    is_active = BooleanProperty(default=True)
    lecture_hours_amount = IntegerProperty()
    exercises_hours_amount = IntegerProperty()
    has_exam = BooleanProperty()
    ECTS = IntegerProperty()
    is_obligatory = BooleanProperty()
    semester = IntegerProperty()
    review = RelationshipFrom('Review', "reviews", cardinality=ZeroOrMore)
    specialization = RelationshipFrom(Specialization, "HAS_COURSE", cardinality=OneOrMore)
    professor_course = RelationshipTo("ProfessorCourse", "IS_TAUGHT_BY")


class ProfessorCourse(StructuredNode):
    uid = UniqueIdProperty()
    is_active = BooleanProperty(default=True)
    course = RelationshipFrom(Course, "IS_TAUGHT_BY", cardinality=ZeroOrOne)
    professor = RelationshipFrom("Professor", "TEACHES", cardinality=ZeroOrOne)
    is_professor_lecturer = BooleanProperty(required=True)
    review = RelationshipFrom('Review', "reviews")


class Professor(StructuredNode):
    uid = UniqueIdProperty()
    first_name = StringProperty(max_length=100)
    last_name = StringProperty(max_length=100)
    is_active = BooleanProperty(default=True)
    birth_year = IntegerProperty()
    is_male = BooleanProperty(required=True)
    degree = StringProperty(required=True, choices=DEGREES)
    professor_course = RelationshipTo(ProfessorCourse, "TEACHES", cardinality=ZeroOrMore)


class ReactsTo(StructuredRel):
    reaction = StringProperty(choices={'L': "like", 'D': "dislike"}, required=True)


class User(StructuredNode):
    uid = UniqueIdProperty()
    is_active = BooleanProperty(default=True)
    username = StringProperty(max_length=100, required=True)
    salt = StringProperty(max_length=150, required=True)
    password = StringProperty(max_length=150, required=True)
    most_recent_login_timestamp = DateTimeProperty()
    email_address = EmailProperty()
    is_staff = BooleanProperty(default=False)
    is_super_user = BooleanProperty(default=False)
    first_name = StringProperty(max_length=100)
    last_name = StringProperty(max_length=100)
    date_joined = DateTimeProperty(default_now=True)
    birthday = DateProperty()
    course = RelationshipTo(ProfessorCourse, "TAKES_PART_IN", cardinality=ZeroOrMore)
    specialization = RelationshipTo(Specialization, "STUDIES", cardinality=ZeroOrMore)
    reactsToReview = RelationshipTo('Review', "REACTS_TO", model=ReactsTo, cardinality=ZeroOrMore)
    reactsToReply = RelationshipTo('Reply', "REACTS_TO", model=ReactsTo, cardinality=ZeroOrMore)


class Tag(StructuredNode):
    uid = UniqueIdProperty()
    tag = StringProperty(max_length=50, required=True)


class Review(StructuredNode):
    uid = UniqueIdProperty()
    is_text_visible = BooleanProperty(required=True)
    text = StringProperty(max_length=3000)
    QUALITY = {1: "The worst", 2: "bad", 3: "ok", 4: "good", 5: "great"}
    quality = StringProperty(choices=QUALITY, required=True)
    DIFFICULTY = {1: "Very difficult", 2: "difficult", 3: "moderate", 4: "easy", 5: "very easy"}
    difficulty = StringProperty(choices=DIFFICULTY, required=False)
    author = RelationshipFrom(User, "CREATED_REVIEW", cardinality=One)
    # if by mistake you put a `required=True` as argument to RelationshipFrom,
    # it will throw exception `neomodel.exceptions.NodeClassAlreadyDefined: <exception str() failed>`
    # instead use cardinality
    tag = RelationshipTo(Tag, "IS_TAGGED", cardinality=ZeroOrMore)
    creation_date = DateTimeProperty(default_now=True)
    most_recent_edit_date = DateTimeProperty()


class Reply(StructuredNode):
    uid = UniqueIdProperty()
    is_text_visible = BooleanProperty(required=True)
    text = StringProperty(max_length=3000)
    author = RelationshipFrom(User, "CREATED_REPLY", cardinality=One)
    creation_date = DateTimeProperty(default_now=True)
    most_recent_edit_date = DateTimeProperty()


class ReviewReply(Reply):
    replies_to_review = RelationshipTo(Review, "REPLIES_TO", cardinality=ZeroOrOne)


class ReplyReply(Reply):
    replies_to_reply = RelationshipTo("Reply", "REPLIES_TO", cardinality=ZeroOrOne)


#
# class Country(StructuredNode):
#     code = StringProperty(unique_index=True, required=True)


class Person(StructuredNode):
    uuid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)

    # traverse outgoing IS_FROM relations, inflate to Country objects
    # country = RelationshipTo(Country, 'IS_FROM')
