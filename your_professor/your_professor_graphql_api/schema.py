from ariadne import (QueryType, ObjectType,
                     gql, make_executable_schema)
from ariadne.asgi import GraphQL
from .resolvers import query, mutation, professor_course, professor, region

type_defs = gql("""
    type Query{
        hello: String!
        country(local_language_name: String): Country
        allRegions(amount: Int): [Region!]
        region(uid: String): Region
        allProfessors(amount: Int): [Professor!]!
        allProfessorCourses(amount: Int): [ProfessorCourse!]!
    }
    type Country{
        uid: String!
        local_language_name: String!
        ISO_code_name: String!
        is_active: Boolean!
        regions(amount: Int): [Region!]!
    }
    
    type Region{
        uid: String!
        local_language_name: String!
        name: String!
        is_active: Boolean!
        country: Country!
        cities: [City!]!
    }
    
    type City{
        uid: String!
        local_language_name: String!
        name: String!
        is_active: Boolean!
        universities: [University!]!
    }
    
    type University{
        uid: String!
        local_language_name: String!
        name: String!
        is_active: Boolean!
        founding_year: Int
        faculties: [Faculty!]!
    }
    
    type Faculty{
        uid: String!
        name: String!
        is_active: Boolean!
        specializations: [Specialization!]!
    }
    
    type ScienceDomain{
        uid: String!
        name: String!
        name_in_polish: String
        is_active: Boolean!
    }
    
    type Course{
        uid: String!
        name: String!
        is_active: Boolean!
        lecture_hours_amount: Int!
        exercises_hours_amount: Int!
        has_exam: Boolean!
        ECTS: Int!
        is_obligatory: Boolean!
        semester: Int!
    }
    
    type Specialization{
        uid: String!
        name: String!
        is_active: Boolean!
        is_full_time: Boolean!
        specialization_degree: Int!
        science_domains: [ScienceDomain!]!
        courses: [Course!]!
    }
    
    type Professor{
        uid: String
        is_active: Boolean!
        first_name: String!
        last_name: String!
        birth_year: Int
        is_male: Boolean!
        degree: String!
    }
    
    type ProfessorCourse{
        uid: String!
        is_active: Boolean!
        course: [Course!]!
        professor: Professor!
        is_professor_lecturer: Boolean!
    }
    
    type Mutation{
        updateRegion(uid: String!, 
            local_language_name: String = "",
            name: String = "", is_active: Boolean=None): Boolean!
        connectRegionToCountry(uid: String!,
            country_uid: String!): Boolean!
    }

    
    
""")

schema = make_executable_schema(type_defs,
                                query,
                                mutation,
                                professor_course,
                                professor,
                                region)

app = GraphQL(schema, debug=True)

