import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-example-queries',
  templateUrl: './example-queries.component.html',
  styleUrls: ['./example-queries.component.scss']
})
export class ExampleQueriesComponent implements OnInit {

  constructor() { }


  exampleQueries: string[] = [
    `{
      allCourses{
        is_active
        is_obligatory
        name
        specializations{
          name
        }
        
        
      }
    }
    `
    ,`{
      allUsers{
        birthday{
          day
          month
          year
        }
        email_address
        date_joined
        is_staff
        courses{
          name
          is_obligatory
          is_taught_by{
            is_active
            is_professor_lecturer
            professor{
              first_name
              last_name
            }
          }
        }
      }
    }`,

    `{
      {
        country(local_language_name: "Polska"){
          local_language_name
          ISO_code_name
          is_active
          uid
          regions{
            local_language_name
            name
            is_active
            uid
            cities{
              local_language_name
              name
              is_active
              uid
              universities{
                local_language_name
                name
                is_active
                uid
                founding_year
                faculties{
                  name
                  is_active
                  uid
                  specializations{
                    name
                    is_active
                    is_full_time
                    specialization_degree
                    uid
                    science_domains{
                      name
                      name_in_polish
                      is_active,
                      uid
                    }
                    reviews{
                      author{
                        first_name
                        last_name
                        is_active
                        is_male
                        is_staff
                        is_super_user
                        email_address
                        username
                        birthday{
                        year
                        month
                        day
                      }
                        date_joined
                      }
                      creation_date
                      difficulty
                      quality
                      is_text_visible
                      most_recent_edit_date
                      text
                      uid
                      tags{
                        tag
                        uid
                      }
                      
                    }
                    users{
                      first_name
                      last_name
                      is_active
                      is_male
                      is_staff
                      is_super_user
                      email_address
                      username
                      birthday{
                        year
                        month
                        day
                      }
                      date_joined
                    }
                  }
                  reviews{
                    author{
                      first_name
                      last_name
                      is_active
                      is_male
                      is_staff
                      is_super_user
                      email_address
                      username
                      birthday{
                        year
                        month
                        day
                      }
                      date_joined
                    }
                    creation_date
                    difficulty
                    quality
                    is_text_visible
                    most_recent_edit_date
                    text
                    uid
                    tags{
                      tag
                      uid
                    }
                  }
                }
                 reviews{
                    author{
                      first_name
                      last_name
                      is_active
                      is_male
                      is_staff
                      is_super_user
                      email_address
                      username
                      birthday{
                        year
                        month
                        day
                      }
                      date_joined
                    }
                    creation_date
                    difficulty
                    quality
                    is_text_visible
                    most_recent_edit_date
                    text
                    uid
                    tags{
                      tag
                      uid
                    }
                  }
              }
            }
          }
        }
      }
    }`,
    `
    mutation{
      createCountryByISO(ISO_code_name: "IT", local_language_name: "Italy"){
        country{
          ISO_code_name,
          is_active,
          local_language_name,
          uid
        }
        error
        status
      }
    }    
    `,
    `
    mutation{
      updateCountry(uid: "3563831de98c4c3dbe93d80bb0d7ffd4", is_active: false){
        country{
          ISO_code_name,
          is_active,
          local_language_name,
          uid
        }
        error
        status
      }
    }
    `

  ];

  ngOnInit(): void {
  }

}
