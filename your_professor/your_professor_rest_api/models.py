from django.db import models

# Create your models here.

from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, RelationshipFrom, BooleanProperty,
                      EmailProperty, DateTimeProperty, DateProperty, Relationship, StructuredRel)


# config.DATABASE_URL = 'bolt://neo4j:3BejhhmCyUa4oPLm2XAgmX8GcsGqipFf9EtQvmPuo@localhost:7687'


class Country(StructuredNode):
    uid = UniqueIdProperty()
    ISO_code_name = StringProperty(choices={
        "Andorra": "AD",
        "United Arab Emirates (the)": "AE",
        "Afghanistan": "AF",
        "Antigua and Barbuda": "AG",
        "Anguilla": "AI",
        "Albania": "AL",
        "Armenia": "AM",
        "Angola": "AO",
        "Antarctica": "AQ",
        "Argentina": "AR",
        "American Samoa": "AS",
        "Austria": "AT",
        "Australia": "AU",
        "Aruba": "AW",
        "Åland Islands": "AX",
        "Azerbaijan": "AZ",
        "Bosnia and Herzegovina": "BA",
        "Barbados": "BB",
        "Bangladesh": "BD",
        "Belgium": "BE",
        "Burkina Faso": "BF",
        "Bulgaria": "BG",
        "Bahrain": "BH",
        "Burundi": "BI",
        "Benin": "BJ",
        "Saint Barthélemy": "BL",
        "Bermuda": "BM",
        "Brunei Darussalam": "BN",
        "Bolivia (Plurinational State of)": "BO",
        "Bonaire, Sint Eustatius and Saba": "BQ",
        "Brazil": "BR",
        "Bahamas (the)": "BS",
        "Bhutan": "BT",
        "Bouvet Island": "BV",
        "Botswana": "BW",
        "Belarus": "BY",
        "Belize": "BZ",
        "Canada": "CA",
        "Cocos (Keeling) Islands (the)": "CC",
        "Congo (the Democratic Republic of the)": "CD",
        "Central African Republic (the)": "CF",
        "Congo (the)": "CG",
        "Switzerland": "CH",
        "Côte d'Ivoire": "CI",
        "Cook Islands (the)": "CK",
        "Chile": "CL",
        "Cameroon": "CM",
        "China": "CN",
        "Colombia": "CO",
        "Costa Rica": "CR",
        "Cuba": "CU",
        "Cabo Verde": "CV",
        "Curaçao": "CW",
        "Christmas Island": "CX",
        "Cyprus": "CY",
        "Czechia": "CZ",
        "Germany": "DE",
        "Djibouti": "DJ",
        "Denmark": "DK",
        "Dominica": "DM",
        "Dominican Republic (the)": "DO",
        "Algeria": "DZ",
        "Ecuador": "EC",
        "Estonia": "EE",
        "Egypt": "EG",
        "Western Sahara": "EH",
        "Eritrea": "ER",
        "Spain": "ES",
        "Ethiopia": "ET",
        "Finland": "FI",
        "Fiji": "FJ",
        "Falkland Islands (the) [Malvinas]": "FK",
        "Micronesia (Federated States of)": "FM",
        "Faroe Islands (the)": "FO",
        "France": "FR",
        "Gabon": "GA",
        "United Kingdom of Great Britain and Northern Ireland (the)": "GB",
        "Grenada": "GD",
        "Georgia": "GE",
        "French Guiana": "GF",
        "Guernsey": "GG",
        "Ghana": "GH",
        "Gibraltar": "GI",
        "Greenland": "GL",
        "Gambia (the)": "GM",
        "Guinea": "GN",
        "Guadeloupe": "GP",
        "Equatorial Guinea": "GQ",
        "Greece": "GR",
        "South Georgia and the South Sandwich Islands": "GS",
        "Guatemala": "GT",
        "Guam": "GU",
        "Guinea-Bissau": "GW",
        "Guyana": "GY",
        "Hong Kong": "HK",
        "Heard Island and McDonald Islands": "HM",
        "Honduras": "HN",
        "Croatia": "HR",
        "Haiti": "HT",
        "Hungary": "HU",
        "Indonesia": "ID",
        "Ireland": "IE",
        "Israel": "IL",
        "Isle of Man": "IM",
        "India": "IN",
        "British Indian Ocean Territory (the)": "IO",
        "Iraq": "IQ",
        "Iran (Islamic Republic of)": "IR",
        "Iceland": "IS",
        "Italy": "IT",
        "Jersey": "JE",
        "Jamaica": "JM",
        "Jordan": "JO",
        "Japan": "JP",
        "Kenya": "KE",
        "Kyrgyzstan": "KG",
        "Cambodia": "KH",
        "Kiribati": "KI",
        "Comoros (the)": "KM",
        "Saint Kitts and Nevis": "KN",
        "Korea (the Democratic People's Republic of)": "KP",
        "Korea (the Republic of)": "KR",
        "Kuwait": "KW",
        "Cayman Islands (the)": "KY",
        "Kazakhstan": "KZ",
        "Lao People's Democratic Republic (the)": "LA",
        "Lebanon": "LB",
        "Saint Lucia": "LC",
        "Liechtenstein": "LI",
        "Sri Lanka": "LK",
        "Liberia": "LR",
        "Lesotho": "LS",
        "Lithuania": "LT",
        "Luxembourg": "LU",
        "Latvia": "LV",
        "Libya": "LY",
        "Morocco": "MA",
        "Monaco": "MC",
        "Moldova (the Republic of)": "MD",
        "Montenegro": "ME",
        "Saint Martin (French part)": "MF",
        "Madagascar": "MG",
        "Marshall Islands (the)": "MH",
        "Republic of North Macedonia": "MK",
        "Mali": "ML",
        "Myanmar": "MM",
        "Mongolia": "MN",
        "Macao": "MO",
        "Northern Mariana Islands (the)": "MP",
        "Martinique": "MQ",
        "Mauritania": "MR",
        "Montserrat": "MS",
        "Malta": "MT",
        "Mauritius": "MU",
        "Maldives": "MV",
        "Malawi": "MW",
        "Mexico": "MX",
        "Malaysia": "MY",
        "Mozambique": "MZ",
        "Namibia": "NA",
        "New Caledonia": "NC",
        "Niger (the)": "NE",
        "Norfolk Island": "NF",
        "Nigeria": "NG",
        "Nicaragua": "NI",
        "Netherlands (the)": "NL",
        "Norway": "NO",
        "Nepal": "NP",
        "Nauru": "NR",
        "Niue": "NU",
        "New Zealand": "NZ",
        "Oman": "OM",
        "Panama": "PA",
        "Peru": "PE",
        "French Polynesia": "PF",
        "Papua New Guinea": "PG",
        "Philippines (the)": "PH",
        "Pakistan": "PK",
        "Poland": "PL",
        "Saint Pierre and Miquelon": "PM",
        "Pitcairn": "PN",
        "Puerto Rico": "PR",
        "Palestine, State of": "PS",
        "Portugal": "PT",
        "Palau": "PW",
        "Paraguay": "PY",
        "Qatar": "QA",
        "Réunion": "RE",
        "Romania": "RO",
        "Serbia": "RS",
        "Russian Federation (the)": "RU",
        "Rwanda": "RW",
        "Saudi Arabia": "SA",
        "Solomon Islands": "SB",
        "Seychelles": "SC",
        "Sudan (the)": "SD",
        "Sweden": "SE",
        "Singapore": "SG",
        "Saint Helena, Ascension and Tristan da Cunha": "SH",
        "Slovenia": "SI",
        "Svalbard and Jan Mayen": "SJ",
        "Slovakia": "SK",
        "Sierra Leone": "SL",
        "San Marino": "SM",
        "Senegal": "SN",
        "Somalia": "SO",
        "Suriname": "SR",
        "South Sudan": "SS",
        "Sao Tome and Principe": "ST",
        "El Salvador": "SV",
        "Sint Maarten (Dutch part)": "SX",
        "Syrian Arab Republic": "SY",
        "Eswatini": "SZ",
        "Turks and Caicos Islands (the)": "TC",
        "Chad": "TD",
        "French Southern Territories (the)": "TF",
        "Togo": "TG",
        "Thailand": "TH",
        "Tajikistan": "TJ",
        "Tokelau": "TK",
        "Timor-Leste": "TL",
        "Turkmenistan": "TM",
        "Tunisia": "TN",
        "Tonga": "TO",
        "Turkey": "TR",
        "Trinidad and Tobago": "TT",
        "Tuvalu": "TV",
        "Taiwan (Province of China)": "TW",
        "Tanzania, United Republic of": "TZ",
        "Ukraine": "UA",
        "Uganda": "UG",
        "United States Minor Outlying Islands (the)": "UM",
        "United States of America (the)": "US",
        "Uruguay": "UY",
        "Uzbekistan": "UZ",
        "Holy See (the)": "VA",
        "Saint Vincent and the Grenadines": "VC",
        "Venezuela (Bolivarian Republic of)": "VE",
        "Virgin Islands (British)": "VG",
        "Virgin Islands (U.S.)": "VI",
        "Viet Nam": "VN",
        "Vanuatu": "VU",
        "Wallis and Futuna": "WF",
        "Samoa": "WS",
        "Yemen": "YE",
        "Mayotte": "YT",
        "South Africa": "ZA",
        "Zambia": "ZM",
        "Zimbabwe": "ZW",
    }, required=True)
    is_active = BooleanProperty(required=True)
    language = StringProperty(max_length=100, required=True)


class Region(StructuredNode):  # example Malopolskie
    uid = UniqueIdProperty()
    name = StringProperty(max_length=100, required=False)
    local_language_name = StringProperty(max_length=100, required=True)
    is_active = BooleanProperty(required=True)
    country = RelationshipFrom(Country, "CONTAINS_REGION")


class City(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(max_length=100)
    is_active = BooleanProperty(required=True)
    region = RelationshipFrom(Region, "CONTAINS CITY")


class University(StructuredNode):  # example University of science and technology or Akademia Gorniczo Hutnicza
    uid = UniqueIdProperty()
    name = StringProperty(max_length=100)
    local_language_name = StringProperty(max_length=100, required=False)
    is_active = BooleanProperty(required=True)
    founding_year = IntegerProperty(required=False)
    city = RelationshipFrom(City, "HOSTS_UNIVERSITY")


class Faculty(StructuredNode):  # example "wydzial fizyki i informatyki stosowanej"
    uid = UniqueIdProperty()
    name = StringProperty(max_length=100)
    is_active = BooleanProperty(required=True)
    university = RelationshipFrom(University, "HAS_FACULTY")


class ScienceDomain(StructuredNode):  # example biology, computer science
    uid = UniqueIdProperty()
    name = StringProperty(max_length=100)
    is_active = BooleanProperty(required=True)


class Course(StructuredNode):  # example "Python in the enterprise" or "Bazy danych 1"
    uid = UniqueIdProperty()
    name = StringProperty(max_length=100)
    is_active = BooleanProperty(required=True)
    lecture_hours_amount = IntegerProperty()
    exercises_hours_amount = IntegerProperty()
    has_exam = BooleanProperty()
    ECTS = IntegerProperty()
    is_obligatory = BooleanProperty()
    semester = IntegerProperty()


class Specialization(StructuredNode):  # example "informatyka stosowana", "fizyka medyczna"
    uid = UniqueIdProperty()
    name = StringProperty(max_length=100)
    is_active = BooleanProperty(required=True)
    is_full_time = BooleanProperty(required=True)
    specialization_degree = IntegerProperty()  # 0 bachelor, 1 master, 2 doctor
    faculty = RelationshipFrom(Faculty, "HAS_SPECIALIZATION")
    science_domain = RelationshipTo(ScienceDomain, "IS_DOMAIN_OF")
    course = RelationshipTo(Course, "HAS_COURSE")


class Professor(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(max_length=100)
    is_active = BooleanProperty(required=True)
    first_name = StringProperty(max_length=100)
    last_name = StringProperty(max_length=100)
    birth_year = IntegerProperty()
    is_male = BooleanProperty(required=True)
    DEGREES = {0: 'no_degree', 1: "bachelor", 2: "master", 3: "doctor"}
    degree = StringProperty(required=True, choices=DEGREES)


class ProfessorCourse(StructuredNode):
    uid = UniqueIdProperty()
    is_active = BooleanProperty(required=True)
    course = RelationshipFrom(Course, "IS_TAUGHT_BY")
    professor = RelationshipFrom(Professor, "TEACHES")
    is_professor_lecturer = BooleanProperty()


class ReactsTo(StructuredRel):
    reaction = StringProperty(choices={1: "like", 0: "dislike"}, required=True)


class User(StructuredNode):
    uid = UniqueIdProperty()
    is_active = BooleanProperty(required=True)
    username = StringProperty(max_length=100, required=True)
    password = StringProperty(max_length=100, required=True)
    most_recent_login_timestamp = DateTimeProperty()
    email_address = EmailProperty()
    is_staff = BooleanProperty(required=True)
    date_joined = DateTimeProperty(default_now=True)
    birthday = DateProperty()
    course = RelationshipTo(ProfessorCourse, "TAKES_PART_IN")
    reactsToReview = RelationshipTo('Review', "REACTS_TO", model=ReactsTo)
    reactsToReply = RelationshipTo('Reply', "REACTS_TO", model=ReactsTo)

#
# class Country(StructuredNode):
#     code = StringProperty(unique_index=True, required=True)

class Person(StructuredNode):
    uuid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)

    # traverse outgoing IS_FROM relations, inflate to Country objects
    # country = RelationshipTo(Country, 'IS_FROM')
