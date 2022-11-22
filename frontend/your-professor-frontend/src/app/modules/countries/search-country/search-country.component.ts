import { Component, OnInit } from '@angular/core';
import { Apollo, gql } from 'apollo-angular';


@Component({
  selector: 'app-search-country',
  templateUrl: './search-country.component.html',
  styleUrls: ['./search-country.component.scss']
})
export class SearchCountryComponent implements OnInit {

  searched_local_language_name: string = '';

  constructor(private apollo: Apollo) { }

  ngOnInit(): void {
  }

  //results: Country = placeholderCountry
  results: any;
  loading: any;
  error: string = '';


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
