from django.db import models

# Create your models here.

from django_neomodel import DjangoNode
from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, RelationshipFrom, BooleanProperty,
                      EmailProperty, DateTimeProperty, DateProperty, Relationship, StructuredRel)


# config.DATABASE_URL = 'bolt://neo4j:3BejhhmCyUa4oPLm2XAgmX8GcsGqipFf9EtQvmPuo@localhost:7687'

# TODO add cardinality to models
# TODO add relation properties similar to class ReactsTo(StructuredRel)

COUNTRIES = {
    "AD": "Andorra",
    "AE": "United Arab Emirates",
    "AF": "Afghanistan",
    "AG": "Antigua and Barbuda",
    "AI": "Anguilla",
    "AL": "Albania",
    "AM": "Armenia",
    "AO": "Angola",
    "AQ": "Antarctica",
    "AR": "Argentina",
    "AS": "American Samoa",
    "AT": "Austria",
    "AU": "Australia",
    "AW": "Aruba",
    "AX": "Åland Islands",
    "AZ": "Azerbaijan",
    "BA": "Bosnia and Herzegovina",
    "BB": "Barbados",
    "BD": "Bangladesh",
    "BE": "Belgium",
    "BF": "Burkina Faso",
    "BG": "Bulgaria",
    "BH": "Bahrain",
    "BI": "Burundi",
    "BJ": "Benin",
    "BL": "Saint Barthélemy",
    "BM": "Bermuda",
    "BN": "Brunei Darussalam",
    "BO": "Bolivia (Plurinational State of)",
    "BQ": "Bonaire, Sint Eustatius and Saba",
    "BR": "Brazil",
    "BS": "Bahamas",
    "BT": "Bhutan",
    "BV": "Bouvet Island",
    "BW": "Botswana",
    "BY": "Belarus",
    "BZ": "Belize",
    "CA": "Canada",
    "CC": "Cocos (Keeling) Islands",
    "CD": "Congo (the Democratic Republic of the)",
    "CF": "Central African Republic",
    "CG": "Congo",
    "CH": "Switzerland",
    "CI": "Côte d'Ivoire",
    "CK": "Cook Islands",
    "CL": "Chile",
    "CM": "Cameroon",
    "CN": "China",
    "CO": "Colombia",
    "CR": "Costa Rica",
    "CU": "Cuba",
    "CV": "Cabo Verde",
    "CW": "Curaçao",
    "CX": "Christmas Island",
    "CY": "Cyprus",
    "CZ": "Czechia",
    "DE": "Germany",
    "DJ": "Djibouti",
    "DK": "Denmark",
    "DM": "Dominica",
    "DO": "Dominican Republic",
    "DZ": "Algeria",
    "EC": "Ecuador",
    "EE": "Estonia",
    "EG": "Egypt",
    "EH": "Western Sahara",
    "ER": "Eritrea",
    "ES": "Spain",
    "ET": "Ethiopia",
    "FI": "Finland",
    "FJ": "Fiji",
    "FK": "Falkland Islands [Malvinas]",
    "FM": "Micronesia (Federated States of)",
    "FO": "Faroe Islands",
    "FR": "France",
    "GA": "Gabon",
    "GB": "United Kingdom of Great Britain and Northern Ireland",
    "GD": "Grenada",
    "GE": "Georgia",
    "GF": "French Guiana",
    "GG": "Guernsey",
    "GH": "Ghana",
    "GI": "Gibraltar",
    "GL": "Greenland",
    "GM": "Gambia",
    "GN": "Guinea",
    "GP": "Guadeloupe",
    "GQ": "Equatorial Guinea",
    "GR": "Greece",
    "GS": "South Georgia and the South Sandwich Islands",
    "GT": "Guatemala",
    "GU": "Guam",
    "GW": "Guinea-Bissau",
    "GY": "Guyana",
    "HK": "Hong Kong",
    "HM": "Heard Island and McDonald Islands",
    "HN": "Honduras",
    "HR": "Croatia",
    "HT": "Haiti",
    "HU": "Hungary",
    "ID": "Indonesia",
    "IE": "Ireland",
    "IL": "Israel",
    "IM": "Isle of Man",
    "IN": "India",
    "IO": "British Indian Ocean Territory",
    "IQ": "Iraq",
    "IR": "Iran (Islamic Republic of)",
    "IS": "Iceland",
    "IT": "Italy",
    "JE": "Jersey",
    "JM": "Jamaica",
    "JO": "Jordan",
    "JP": "Japan",
    "KE": "Kenya",
    "KG": "Kyrgyzstan",
    "KH": "Cambodia",
    "KI": "Kiribati",
    "KM": "Comoros",
    "KN": "Saint Kitts and Nevis",
    "KP": "Korea (the Democratic People's Republic of)",
    "KR": "Korea (the Republic of)",
    "KW": "Kuwait",
    "KY": "Cayman Islands",
    "KZ": "Kazakhstan",
    "LA": "Lao People's Democratic Republic",
    "LB": "Lebanon",
    "LC": "Saint Lucia",
    "LI": "Liechtenstein",
    "LK": "Sri Lanka",
    "LR": "Liberia",
    "LS": "Lesotho",
    "LT": "Lithuania",
    "LU": "Luxembourg",
    "LV": "Latvia",
    "LY": "Libya",
    "MA": "Morocco",
    "MC": "Monaco",
    "MD": "Moldova (the Republic of)",
    "ME": "Montenegro",
    "MF": "Saint Martin (French part)",
    "MG": "Madagascar",
    "MH": "Marshall Islands",
    "MK": "Republic of North Macedonia",
    "ML": "Mali",
    "MM": "Myanmar",
    "MN": "Mongolia",
    "MO": "Macao",
    "MP": "Northern Mariana Islands",
    "MQ": "Martinique",
    "MR": "Mauritania",
    "MS": "Montserrat",
    "MT": "Malta",
    "MU": "Mauritius",
    "MV": "Maldives",
    "MW": "Malawi",
    "MX": "Mexico",
    "MY": "Malaysia",
    "MZ": "Mozambique",
    "NA": "Namibia",
    "NC": "New Caledonia",
    "NE": "Niger",
    "NF": "Norfolk Island",
    "NG": "Nigeria",
    "NI": "Nicaragua",
    "NL": "Netherlands",
    "NO": "Norway",
    "NP": "Nepal",
    "NR": "Nauru",
    "NU": "Niue",
    "NZ": "New Zealand",
    "OM": "Oman",
    "PA": "Panama",
    "PE": "Peru",
    "PF": "French Polynesia",
    "PG": "Papua New Guinea",
    "PH": "Philippines",
    "PK": "Pakistan",
    "PL": "Poland",
    "PM": "Saint Pierre and Miquelon",
    "PN": "Pitcairn",
    "PR": "Puerto Rico",
    "PS": "Palestine, State of",
    "PT": "Portugal",
    "PW": "Palau",
    "PY": "Paraguay",
    "QA": "Qatar",
    "RE": "Réunion",
    "RO": "Romania",
    "RS": "Serbia",
    "RU": "Russian Federation",
    "RW": "Rwanda",
    "SA": "Saudi Arabia",
    "SB": "Solomon Islands",
    "SC": "Seychelles",
    "SD": "Sudan",
    "SE": "Sweden",
    "SG": "Singapore",
    "SH": "Saint Helena, Ascension and Tristan da Cunha",
    "SI": "Slovenia",
    "SJ": "Svalbard and Jan Mayen",
    "SK": "Slovakia",
    "SL": "Sierra Leone",
    "SM": "San Marino",
    "SN": "Senegal",
    "SO": "Somalia",
    "SR": "Suriname",
    "SS": "South Sudan",
    "ST": "Sao Tome and Principe",
    "SV": "El Salvador",
    "SX": "Sint Maarten (Dutch part)",
    "SY": "Syrian Arab Republic",
    "SZ": "Eswatini",
    "TC": "Turks and Caicos Islands",
    "TD": "Chad",
    "TF": "French Southern Territories",
    "TG": "Togo",
    "TH": "Thailand",
    "TJ": "Tajikistan",
    "TK": "Tokelau",
    "TL": "Timor-Leste",
    "TM": "Turkmenistan",
    "TN": "Tunisia",
    "TO": "Tonga",
    "TR": "Turkey",
    "TT": "Trinidad and Tobago",
    "TV": "Tuvalu",
    "TW": "Taiwan (Province of China)",
    "TZ": "Tanzania, United Republic of",
    "UA": "Ukraine",
    "UG": "Uganda",
    "UM": "United States Minor Outlying Islands",
    "US": "United States of America",
    "UY": "Uruguay",
    "UZ": "Uzbekistan",
    "VA": "Holy See",
    "VC": "Saint Vincent and the Grenadines",
    "VE": "Venezuela (Bolivarian Republic of)",
    "VG": "Virgin Islands (British)",
    "VI": "Virgin Islands (U.S.)",
    "VN": "Viet Nam",
    "VU": "Vanuatu",
    "WF": "Wallis and Futuna",
    "WS": "Samoa",
    "YE": "Yemen",
    "YT": "Mayotte",
    "ZA": "South Africa",
    "ZM": "Zambia",
    "ZW": "Zimbabwe",
}


# class Book(StructuredNode):
#     title = StringProperty(unique_index=True)
#     published = DateProperty()
#

class Country(DjangoNode):
    uid = UniqueIdProperty()
    local_language_name = StringProperty(required=True)
    ISO_code_name = StringProperty(choices=COUNTRIES, required=True)
    is_active = BooleanProperty(required=True)
    # language = StringProperty(max_length=100, required=True)
    region = RelationshipTo("Region", "CONTAINS_REGION")


class Region(StructuredNode):  # example Malopolskie
    uid = UniqueIdProperty()
    local_language_name = StringProperty(max_length=100, required=True)
    name = StringProperty(max_length=100, required=False)  # region may not have english version of its name
    is_active = BooleanProperty(required=True)
    country = RelationshipFrom(Country, "CONTAINS_REGION")


class City(StructuredNode):
    uid = UniqueIdProperty()
    local_language_name = StringProperty(required=True)
    name = StringProperty(max_length=100)
    is_active = BooleanProperty(required=True)
    region = RelationshipFrom(Region, "CONTAINS CITY")


class University(StructuredNode):  # example University of science and technology or Akademia Gorniczo Hutnicza
    uid = UniqueIdProperty()
    local_language_name = StringProperty(max_length=100, required=True)
    name = StringProperty(max_length=100)
    is_active = BooleanProperty(default=True)
    founding_year = IntegerProperty(required=False)
    city = RelationshipFrom(City, "HOSTS_UNIVERSITY")
    review = RelationshipFrom('Review', "reviews")


class Faculty(StructuredNode):  # example "wydzial fizyki i informatyki stosowanej"
    uid = UniqueIdProperty()
    name = StringProperty(max_length=100)
    is_active = BooleanProperty(default=True)
    university = RelationshipFrom(University, "HAS_FACULTY")
    review = RelationshipFrom('Review', "reviews")


class ScienceDomain(StructuredNode):  # example biology, computer science
    uid = UniqueIdProperty()
    name = StringProperty(max_length=100, required=True)
    name_in_polish = StringProperty()
    is_active = BooleanProperty(default=True)


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
    review = RelationshipFrom('Review', "reviews")


class Specialization(StructuredNode):  # example "informatyka stosowana", "fizyka medyczna"
    uid = UniqueIdProperty()
    name = StringProperty(max_length=100)
    is_active = BooleanProperty(default=True)
    is_full_time = BooleanProperty(required=True)
    specialization_degree = IntegerProperty()  # 0 bachelor, 1 master, 2 doctor
    faculty = RelationshipFrom(Faculty, "HAS_SPECIALIZATION")
    science_domain = RelationshipTo(ScienceDomain, "IS_PART_OF_DOMAIN")
    course = RelationshipTo(Course, "HAS_COURSE")
    review = RelationshipFrom('Review', "reviews")


class Professor(StructuredNode):
    uid = UniqueIdProperty()
    is_active = BooleanProperty(default=True)
    first_name = StringProperty(max_length=100)
    last_name = StringProperty(max_length=100)
    birth_year = IntegerProperty()
    is_male = BooleanProperty(required=True)
    DEGREES = {'0': 'no_degree', '1': "bachelor", '2': "master", '3': "doctor"}
    degree = StringProperty(required=True, choices=DEGREES)


class ProfessorCourse(StructuredNode):
    uid = UniqueIdProperty()
    is_active = BooleanProperty(default=True)
    course = RelationshipFrom(Course, "IS_TAUGHT_BY")
    professor = RelationshipFrom(Professor, "TEACHES")
    is_professor_lecturer = BooleanProperty(required=True)
    review = RelationshipFrom('Review', "reviews")


class ReactsTo(StructuredRel):
    reaction = StringProperty(choices={1: "like", 0: "dislike"}, required=True)


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
    course = RelationshipTo(ProfessorCourse, "TAKES_PART_IN")
    specialization = RelationshipTo(Specialization, "STUDIES")
    reactsToReview = RelationshipTo('Review', "REACTS_TO", model=ReactsTo)
    reactsToReply = RelationshipTo('Reply', "REACTS_TO", model=ReactsTo)


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
    author = RelationshipFrom(User, "CREATED_REVIEW")
    # if by mistake you put a `required=True` as argument to RelationshipFrom,
    # it will throw exception `neomodel.exceptions.NodeClassAlreadyDefined: <exception str() failed>`
    # instead use cardinality
    tag = RelationshipTo(Tag, "IS_TAGGED")
    creation_date = DateTimeProperty(default_now=True)
    most_recent_edit_date = DateTimeProperty()


class Reply(StructuredNode):
    uid = UniqueIdProperty()
    is_text_visible = BooleanProperty(required=True)
    text = StringProperty(max_length=3000)
    author = RelationshipFrom(User, "CREATED_REPLY")
    replies_to_review = RelationshipTo(Review, "REPLIES_TO")
    replies_to_reply = RelationshipTo("Reply", "REPLIES_TO")
    creation_date = DateTimeProperty(default_now=True)
    most_recent_edit_date = DateTimeProperty()


#
# class Country(StructuredNode):
#     code = StringProperty(unique_index=True, required=True)


class Person(StructuredNode):
    uuid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)

    # traverse outgoing IS_FROM relations, inflate to Country objects
    # country = RelationshipTo(Country, 'IS_FROM')
