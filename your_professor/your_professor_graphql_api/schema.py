from ariadne import (QueryType, ObjectType,
                     gql, make_executable_schema)
from ariadne.asgi import GraphQL
from .resolvers import query, professor_course, professor, region
from .mutation_resolvers.mutation_resolvers import mutation

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
        createCountryByISO(local_language_name: String!,
            ISO_code_name: String!): MutationPayloadCountry!
        updateCountry(uid: String!, 
            local_language_name: String = "", 
            ISO_code_name: String = "", 
            is_active:Boolean = None): MutationPayloadCountry!
        deleteCountry(uid: String!, force: Boolean = False): MutationPayload!
        
        createRegion(local_language_name: String!,
            name: String = "",
            uid_country: String!): MutationPayloadRegion!
        updateRegion(uid: String!, 
            local_language_name: String = "",
            name: String = "", 
            is_active: Boolean=None,
            uid_country: String = ""): Boolean!
        deleteRegion(uid: String!, force: Boolean = False): MutationPayload!
        
        createCity(local_language_name: String!,
            name: String = "",
            is_active: Boolean = None,
            uid_region: String!): MutationPayloadCity!
        updateCity(uid: String!,
            local_language_name: String = "",
            name: String = "",
            is_active: Boolean = None,
            uid_region: String = None): MutationPayloadCity!
        deleteCity(uid: String!, force: Boolean = False): MutationPayload!
        
        createUniversity(local_language_name: String!,
            name: String,
            is_active: Boolean = None,
            founding_year: Int = None,
            uid_city: String!): MutationPayloadUniversity!
        updateUniversity(uid: String!,
            local_language_name: String = None,
            name: String = None,
            is_active: Boolean = None,
            founding_year: Int = None,
            uid_city: String = None): MutationPayloadUniversity!
        deleteUniversity(uid: String!, force: Boolean = False): MutationPayload!
        
        createFaculty(name: String!, is_active: Boolean = None, uid_university: String!): MutationPayloadFaculty!
        updateFaculty(uid: String!, name: String = None, is_active: Boolean = None,
            uid_university: String = None): MutationPayloadFaculty!
        deleteFaculty(uid: String!, force: Boolean = False): MutationPayload!
        
        createSpecialization(name: String!, is_active: Boolean = None, is_full_time: Boolean!, 
            specialization_degree: Int!, uid_faculty: String!): MutationPayloadSpecialization!
        updateSpecialization(uid: String!, name: String, is_active: Boolean = None, is_full_time: Boolean, 
            specialization_degree: Int, uid_faculty: String): MutationPayloadSpecialization!
        deleteSpecialization(uid: String!, force: Boolean = False): MutationPayload!
        
    }
    
    type MutationPayload{
        status: Boolean!
        error: String
    }
    
    type MutationPayloadCountry{
        status: Boolean!
        error: String
        country: Country
    }
    
    type MutationPayloadRegion{
        status: Boolean!
        error: String
        region: Region
    }
    
    type MutationPayloadCity{
        status: Boolean!
        error: String
        city: City
    }
    
    type MutationPayloadUniversity{
        status: Boolean!
        error: String
        university: University
    }
    
    type MutationPayloadFaculty{
        status: Boolean!
        error: String
        faculty: Faculty
    }
    
    type MutationPayloadSpecialization{
        status: Boolean!
        error: String
        specialization: Specialization
    }
    
    
""")

schema = make_executable_schema(type_defs,
                                query,
                                mutation,
                                professor_course,
                                professor,
                                region)

app = GraphQL(schema, debug=True)

