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
    }`

  ];

  ngOnInit(): void {
  }

}
