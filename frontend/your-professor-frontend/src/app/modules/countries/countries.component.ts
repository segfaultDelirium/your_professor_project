import { Component, OnInit } from '@angular/core';
import { Apollo, gql } from 'apollo-angular';


// export type Country = {
//   local_language_name: string
//   ISO_code_name: string
//   is_active: boolean | undefined
// }

// const placeholderCountry: Country = {
//   local_language_name: "",
//   ISO_code_name: '',
//   is_active: undefined
// }

@Component({
  selector: 'app-countries',
  templateUrl: './countries.component.html',
  styleUrls: ['./countries.component.scss']
})
export class CountriesComponent implements OnInit {


  constructor(private apollo: Apollo) { }

  ngOnInit(): void {
  }


}
