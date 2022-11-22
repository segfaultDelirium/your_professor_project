import { Component, OnDestroy, OnInit } from '@angular/core';
import { Apollo, gql } from 'apollo-angular';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-list-countries',
  templateUrl: './list-countries.component.html',
  styleUrls: ['./list-countries.component.scss']
})
export class ListCountriesComponent implements OnInit, OnDestroy {


  constructor(private apollo: Apollo) { }

  ngOnInit(): void {
    this.query();
  }

  countries: any;
  loading: any;
  error: string = '';

  apolloSubscription?: Subscription;

  query(){
    this.apolloSubscription?.unsubscribe();
    this.apolloSubscription = this.apollo
      .watchQuery({
        query: gql`
        {
          allCountries{
            local_language_name
            ISO_code_name
            is_active    
            uid
            
          }
        }
        `,
      })
      .valueChanges.subscribe((result: any) => {
        console.log(result);
        this.countries = result?.data.allCountries;
        this.loading = result.loading;
        console.log(this.countries)
      });
  }

  ngOnDestroy(): void {
    this.apolloSubscription?.unsubscribe();
  }

}
