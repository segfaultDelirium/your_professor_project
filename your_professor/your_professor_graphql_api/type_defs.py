from ariadne import gql
from .constants import REVIEWED_NODE_TYPE, unpack_dict_values_to_schema_enum, unpack_dict_keys_to_schema_enum, QUALITY
type_defs = gql(f"""
    type Query{{
        country(local_language_name: String): Country
        allCountries(amount: Int): [Country!]!
        region(uid: String): Region
        allRegions(amount: Int): [Region!]
        city(uid: String!): City
        allCities(amount: Int): [City!]
        university(uid: String!): University
        allUniversities(amount: Int): [University!]
        faculty(uid: String!): Faculty
        allFaculties(amount: Int): [Faculty!]
        specialization(uid: String!): Specialization
        allSpecializations(amount: Int): [Specialization!]
        scienceDomain(uid: String!): ScienceDomain
        allScienceDomains(amount: Int): [ScienceDomain!]
        course(uid: String!): Course
        allCourses(amount: Int): [Course!]
        # professorCourse(uid: String!): ProfessorCourse
        # allProfessorCourses(amount: Int): [ProfessorCourse!]
        professor(uid: String!): Professor
        allProfessors(amount: Int): [Professor!]
        user(uid: String!): User
        allUsers(amount: Int): [User!] 
        tag(uid: String!): Tag
        allTags(amount: Int): [Tag!]
        review(uid: String!): Review
        allReviews(amount: Int): [Review!]
    }}
    type Country{{
        uid: String!
        local_language_name: String!
        ISO_code_name: String!
        is_active: Boolean!
        regions(amount: Int): [Region!]
    }}

    type Region{{
        uid: String!
        local_language_name: String!
        name: String!
        is_active: Boolean!
        country: Country!
        cities: [City!]!
    }}

    type City{{
        uid: String!
        local_language_name: String!
        name: String!
        is_active: Boolean!
        universities: [University!]!
        region: Region!
    }}

    type University{{
        uid: String!
        local_language_name: String!
        name: String!
        is_active: Boolean!
        founding_year: Int
        faculties: [Faculty!]
        city: City!
        reviews: [Review!]
    }}

    type Faculty{{
        uid: String!
        name: String!
        is_active: Boolean!
        specializations: [Specialization!]!
        university: University!
        reviews: [Review!]
    }}

    type Specialization{{
        uid: String!
        name: String!
        is_active: Boolean!
        is_full_time: Boolean!
        specialization_degree: Int!
        science_domains: [ScienceDomain!]!
        courses: [Course!]!
        faculty: Faculty!
        users: [User!]
        reviews: [Review!]
    }}

    type ScienceDomain{{
        uid: String!
        name: String!
        name_in_polish: String
        is_active: Boolean!
        specializations: [Specialization!]
    }}

type TeachesDetails{{
        is_active: Boolean
        is_professor_lecturer: Boolean!
        course: Course
        professor: Professor
}}

 input ProfessorTeachesDetails{{
        uid_course: String!
        is_active: Boolean
        is_professor_lecturer: Boolean!
}}


    type Course{{
        uid: String!
        name: String!
        is_active: Boolean!
        lecture_hours_amount: Int!
        exercises_hours_amount: Int!
        has_exam: Boolean!
        ECTS: Int!
        is_obligatory: Boolean!
        semester: Int!
        specializations: [Specialization!]!
        users: [User!]
        reviews: [Review!]
        is_taught_by: [TeachesDetails!]
    }}
 

    type Professor{{
        uid: String
        is_active: Boolean!
        first_name: String!
        last_name: String!
        birth_year: Int
        is_male: Boolean!
        degree: String!
        teaches: [TeachesDetails!]
    }}

 

    scalar Datetime

    type Date{{
        year: Int!
        month: Int!
        day: Int!
    }}

    type User{{
        uid: String!
        is_active: Boolean!
        username: String!
        email_address: String
        is_staff: Boolean!
        is_super_user: Boolean!
        first_name: String
        last_name: String
        date_joined: Datetime!
        birthday: Date
        is_male: Boolean
        courses: [Course!]
        specializations: [Specialization!]
    }}

    type Tag{{
        uid: String!
        tag: String!
        reviews: [Review!]
    }}
    
    enum ReviewedNodeType{{
        {unpack_dict_values_to_schema_enum(REVIEWED_NODE_TYPE)}
        # University
        # Faculty
        # Specialization
        # Course
        # Professor
    }}

    
    type Review{{
        uid: String!
        is_text_visible: Boolean!
        text: String
        quality: String!
        difficulty: String
        author: User!
        tags: [Tag!]
        creation_date: Datetime!
        most_recent_edit_date: Datetime
        reviewed_node_type: ReviewedNodeType!
        reviewed_node_uid: String!
    }}

    type Mutation{{
        createCountryByISO(local_language_name: String!,
            ISO_code_name: String!): MutationPayloadCountry!
        updateCountry(uid: String!, 
            local_language_name: String = "", 
            ISO_code_name: String = "", 
            is_active:Boolean = None): MutationPayloadCountry!
        deleteCountry(uid: String!, force: Boolean = False): MutationPayload!

        createRegion(local_language_name: String!,
            name: String = "",
            uid_country: String!,
            is_active: Boolean): MutationPayloadRegion!
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

        createScienceDomain(name: String!, name_in_polish: String, is_active: Boolean): MutationPayloadScienceDomain!
        updateScienceDomain(uid: String!, name: String, name_in_polish: String, 
            is_active: Boolean): MutationPayloadScienceDomain!
        connectScienceDomainToSpecialization(uid: String!, uid_specialization: String!): MutationPayloadScienceDomain!
        disconnectScienceDomainFromSpecialization(uid: String!, 
            uid_specialization: String!): MutationPayloadScienceDomain!
        deleteScienceDomain(uid: String!, force: Boolean = False): MutationPayload!

        createCourse(name: String!, is_active: Boolean = None, lecture_hours_amount: Int!, 
            exercises_hours_amount: Int!, has_exam: Boolean!, ECTS: Int!, is_obligatory: Boolean!, semester: Int!,
             uid_specialization: String!): MutationPayloadCourse! 
        updateCourse(uid: String!, name: String = None, is_active: Boolean = None, lecture_hours_amount: Int = None, 
            exercises_hours_amount: Int = None, has_exam: Boolean = None, ECTS: Int = None, 
            is_obligatory: Boolean = None, semester: Int = None, 
            uid_specialization: String = None): MutationPayloadCourse!
        deleteCourse(uid: String!, force: Boolean = False): MutationPayload!

        # createProfessorCourse(is_active: Boolean = None, uid_course: String!, uid_professor: String = None,
        #     is_professor_lecturer: Boolean!): MutationPayloadProfessorCourse! 
        # updateProfessorCourse(uid: String!, is_active: Boolean = None, uid_course: String = None, 
        #     uid_professor: String = None, is_professor_lecturer: Boolean = None): MutationPayloadProfessorCourse!
        # deleteProfessorCourse(uid: String!, force: Boolean = False): MutationPayload!

        createProfessor(first_name: String!, last_name: String!, is_active: Boolean = None, birth_year: Int = None, 
            is_male: Boolean!, degree: String!, professor_teaches_details_list: [ProfessorTeachesDetails!] = None): MutationPayloadProfessor!
        updateProfessor(uid: String!, is_active: Boolean = None, first_name: String = None, last_name: String = None, 
            birth_year: Int = None, is_male: Boolean = None, degree: String!, 
            uid_professor_course: String = None): MutationPayloadProfessor!
        # connectProfessorToProfessorCourse(uid: String!, uid_professor_course: String!): MutationPayloadProfessor!
        # reconnectProfessorToProfessorCourse(uid: String!, uid_old_professor_course: String!, 
        #     uid_new_professor_course: String!): MutationPayloadProfessor!
        # disconnectProfessorFromProfessorCourse(uid: String!, uid_professor_course: String!): MutationPayloadProfessor!
        deleteProfessor(uid: String!): MutationPayload!

        createUser(is_active: Boolean, username: String!, password: String!, email_address: String, is_staff: Boolean, 
            is_super_user: Boolean, first_name: String, last_name: String, birthday: Datetime, 
            is_male: Boolean): MutationPayloadUser!
        updateUser(uid: String!, is_active: Boolean, username: String, password: String, email_address: String, 
            is_staff: Boolean, is_super_user: Boolean, first_name: String, last_name: String, birthday: Datetime, 
            is_male: Boolean): MutationPayloadUser! 
        connectUserToSpecialization(uid: String!, uid_specialization: String!): MutationPayloadUser!
        disconnectUserFromSpecialization(uid: String!, uid_specialization: String!): MutationPayloadUser!
        connectUserToCourse(uid: String!, uid_course: String!): MutationPayloadUser!
        disconnectUserFromCourse(uid: String!, uid_course: String!): MutationPayloadUser!
        deleteUser(uid: String!): MutationPayload!
        
        createTag(tag: String!): MutationPayloadTag!
        updateTag(uid: String!, tag: String!): MutationPayloadTag!
        deleteTag(uid: String!): MutationPayload!
        
        createReview(is_text_visible: Boolean, text: String, quality: String!, difficulty: String, uid_author: String!,
            tags: [String!], creation_date: Datetime, reviewed_node_type: ReviewedNodeType!, 
            reviewed_node_uid: String!): MutationPayloadReview!
        updateReview(uid: String!, is_text_visible: Boolean, text: String, quality: String, difficulty: String,
            tags: [String!]): MutationPayloadReview!
        connectReviewToTags(uid: String!, uid_tags: [String!]!): MutationPayloadReview!
        disconnectReviewFromTags(uid: String!, uid_tags: [String!]!): MutationPayloadReview!
        deleteReview(uid: String!): MutationPayload!
    }}

    type MutationPayload{{
        status: Boolean!
        error: String
    }}

    type MutationPayloadCountry{{
        status: Boolean!
        error: String
        country: Country
    }}

    type MutationPayloadRegion{{
        status: Boolean!
        error: String
        region: Region
    }}

    type MutationPayloadCity{{
        status: Boolean!
        error: String
        city: City
    }}

    type MutationPayloadUniversity{{
        status: Boolean!
        error: String
        university: University
    }}

    type MutationPayloadFaculty{{
        status: Boolean!
        error: String
        faculty: Faculty
    }}

    type MutationPayloadSpecialization{{
        status: Boolean!
        error: String
        specialization: Specialization
    }}

    type MutationPayloadScienceDomain{{
        status: Boolean!
        error: String
        science_domain: ScienceDomain
    }}
    type MutationPayloadCourse{{
        status: Boolean!
        error: String
        course: Course
    }}

    type MutationPayloadProfessor{{
        status: Boolean!
        error: String
        professor: Professor
    }}

    type MutationPayloadUser{{
        status: Boolean!
        error: String
        user: User
    }}
    
    type MutationPayloadTag{{
        status: Boolean!
        error: String
        tag: Tag
    }}
    
    type MutationPayloadReview{{
        status: Boolean!
        error: String
        review: Review
    }}


""")