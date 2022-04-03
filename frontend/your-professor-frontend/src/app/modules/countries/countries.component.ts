import { Component, OnInit } from '@angular/core';
import {Apollo, gql} from 'apollo-angular';

@Component({
  selector: 'app-countries',
  templateUrl: './countries.component.html',
  styleUrls: ['./countries.component.scss']
})
export class CountriesComponent implements OnInit {
  results: any;
  loading = true;
  error: any;

  constructor(private apollo: Apollo) {}
  ngOnInit(): void {
    this.query();
  }

  query(){
    this.apollo
      .watchQuery({
        query: gql`
          {
            allCountries{
              local_language_name
            }
          }
        `,
      })
      .valueChanges.subscribe((result: any) => {
        this.results = result?.data;
        this.loading = result.loading;
        this.error = result.error;
        console.log(this.results)
      });
  }

}
