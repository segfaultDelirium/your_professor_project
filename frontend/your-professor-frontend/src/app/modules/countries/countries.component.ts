import { Component, OnInit } from '@angular/core';
import { Apollo, gql } from 'apollo-angular';


export type Country = {
  local_language_name: string
  ISO_code_name: string
  is_active: boolean | undefined
}

const placeholderCountry: Country = {
  local_language_name: "",
  ISO_code_name: '',
  is_active: undefined
}

@Component({
  selector: 'app-countries',
  templateUrl: './countries.component.html',
  styleUrls: ['./countries.component.scss']
})
export class CountriesComponent implements OnInit {

  searched_local_language_name: string = '';

  constructor(private apollo: Apollo) { }

  ngOnInit(): void {
  }

  //results: Country = placeholderCountry
  results: any;
  loading: any;
  error: any;


  queryByLocalLanguageName(local_language_name: string){
    let result = this.apollo
      .watchQuery({
        query: gql`
          {
            country(local_language_name: "${local_language_name}"){
              local_language_name
              ISO_code_name
              is_active
            }
          }
        `,
      })
      .valueChanges.subscribe((result: any) => {
        this.results = result?.data.country;
        this.loading = result.loading;
        this.error = result.error;
        console.log(this.results)
      });
  }

}
