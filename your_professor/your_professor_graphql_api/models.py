from django.db import models
from .constants import DEGREES, COUNTRIES, QUALITY, DIFFICULTY, REVIEWED_NODE_TYPE
from enum import Enum
# Create your models here.

from django_neomodel import DjangoNode
from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, RelationshipFrom, BooleanProperty,
                      EmailProperty, DateTimeProperty, DateProperty, Relationship, StructuredRel,
                      ZeroOrMore, One, ZeroOrOne, OneOrMore)

# update neo4j models:
# neomodel_install_labels  your_professor_graphql_api/models.py --db bolt://neo4j:3BejhhmCyUa4oPLm2XAgmX8GcsGqipFf9EtQvmPuo@localhost:7687/neo4j

# TODO add cardinality to models
# TODO add relation properties similar to class ReactsTo(StructuredRel)


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


class ReviewableNode(StructuredNode):
    reviews = RelationshipFrom('Review', "REVIEWS", cardinality=ZeroOrMore)


class University(ReviewableNode):  # example University of science and technology or Akademia Gorniczo Hutnicza
    uid = UniqueIdProperty()
    local_language_name = StringProperty(max_length=100, required=True)
    name = StringProperty(max_length=100)
    is_active = BooleanProperty(default=True)
    founding_year = IntegerProperty(required=False)
    city = RelationshipFrom(City, "HOSTS_UNIVERSITY", cardinality=One)
    # reviews = RelationshipFrom('Review', "REVIEWS", cardinality=ZeroOrMore)
    faculties = RelationshipTo("Faculty", "HAS_FACULTY", cardinality=ZeroOrMore)


class Faculty(ReviewableNode):  # example "wydzial fizyki i informatyki stosowanej"
    uid = UniqueIdProperty()
    name = StringProperty(max_length=100)
    is_active = BooleanProperty(default=True)
    university = RelationshipFrom(University, "HAS_FACULTY", cardinality=One)
    # reviews = RelationshipFrom('Review', "REVIEWS", cardinality=ZeroOrMore)
    specializations = RelationshipTo("Specialization", "HAS_SPECIALIZATION", cardinality=ZeroOrMore)


class Specialization(ReviewableNode):  # example "informatyka stosowana", "fizyka medyczna"
    uid = UniqueIdProperty()
    name = StringProperty(max_length=100)
    is_active = BooleanProperty(default=True)
    is_full_time = BooleanProperty(required=True)
    specialization_degree = IntegerProperty()  # 0 bachelor, 1 master, 2 doctor
    faculty = RelationshipFrom(Faculty, "HAS_SPECIALIZATION", cardinality=One)
    science_domains = RelationshipTo("ScienceDomain", "IS_PART_OF_DOMAIN", cardinality=ZeroOrMore)
    courses = RelationshipTo("Course", "HAS_COURSE", cardinality=ZeroOrMore)
    # reviews = RelationshipFrom('Review', "REVIEWS", cardinality=ZeroOrMore)
    users = RelationshipFrom("User", "STUDIES", cardinality=ZeroOrMore)


class ScienceDomain(StructuredNode):  # example biology, computer science
    uid = UniqueIdProperty()
    name = StringProperty(max_length=100, required=True)
    name_in_polish = StringProperty()
    is_active = BooleanProperty(default=True)
    specializations = RelationshipFrom(Specialization, "IS_PART_OF_DOMAIN", cardinality=ZeroOrMore)


class Course(ReviewableNode):  # example "Python in the enterprise" or "Bazy danych 1"
    uid = UniqueIdProperty()
    name = StringProperty(max_length=100)
    is_active = BooleanProperty(default=True)
    lecture_hours_amount = IntegerProperty()
    exercises_hours_amount = IntegerProperty()
    has_exam = BooleanProperty()
    ECTS = IntegerProperty()
    is_obligatory = BooleanProperty()
    semester = IntegerProperty()
    # reviews = RelationshipFrom('Review', "REVIEWS", cardinality=ZeroOrMore)
    specializations = RelationshipFrom(Specialization, "HAS_COURSE", cardinality=OneOrMore)
    professor_courses = RelationshipTo("ProfessorCourse", "IS_TAUGHT_BY")
    users = RelationshipFrom("User", "TAKES_PART_IN", cardinality=ZeroOrMore)


class ProfessorCourse(ReviewableNode):
    uid = UniqueIdProperty()
    is_active = BooleanProperty(default=True)
    course = RelationshipFrom(Course, "IS_TAUGHT_BY", cardinality=ZeroOrOne)
    professor = RelationshipFrom("Professor", "TEACHES", cardinality=ZeroOrOne)
    is_professor_lecturer = BooleanProperty(required=True)
    # reviews = RelationshipFrom('Review', "REVIEWS")


class Professor(StructuredNode):
    uid = UniqueIdProperty()
    first_name = StringProperty(max_length=100)
    last_name = StringProperty(max_length=100)
    is_active = BooleanProperty(default=True)
    birth_year = IntegerProperty()
    is_male = BooleanProperty(required=True)
    degree = StringProperty(required=True, choices=DEGREES)
    professor_courses = RelationshipTo(ProfessorCourse, "TEACHES")


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
    is_male = BooleanProperty()
    course = RelationshipTo(Course, "TAKES_PART_IN", cardinality=ZeroOrMore)
    specialization = RelationshipTo(Specialization, "STUDIES", cardinality=ZeroOrMore)
    reactsToReview = RelationshipTo('Review', "REACTS_TO", model=ReactsTo, cardinality=ZeroOrMore)
    reactsToReply = RelationshipTo('Reply', "REACTS_TO", model=ReactsTo, cardinality=ZeroOrMore)
    reviews = RelationshipTo("Review", "CREATED_REVIEW", cardinality=ZeroOrMore)


class Tag(StructuredNode):
    uid = UniqueIdProperty()
    tag = StringProperty(max_length=50, required=True)
    reviews = RelationshipFrom("Review", "IS_TAGGED", cardinality=ZeroOrMore)


class Review(StructuredNode):
    uid = UniqueIdProperty()
    is_text_visible = BooleanProperty(default=True)
    text = StringProperty(max_length=3000)
    quality = StringProperty(choices=QUALITY, required=True)
    difficulty = StringProperty(choices=DIFFICULTY, required=False)
    author = RelationshipFrom(User, "CREATED_REVIEW", cardinality=One)
    tags = RelationshipTo(Tag, "IS_TAGGED", cardinality=ZeroOrMore)
    creation_date = DateTimeProperty(default_now=True)
    most_recent_edit_date = DateTimeProperty()
    reviewed_node_type = StringProperty(choices=REVIEWED_NODE_TYPE, required=True)
    reviewed_node = RelationshipTo(ReviewableNode, "REVIEWS", cardinality=ZeroOrMore)



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

# traverse outgoing IS_FROM relations, inflate to Country objects
# country = RelationshipTo(Country, 'IS_FROM')
