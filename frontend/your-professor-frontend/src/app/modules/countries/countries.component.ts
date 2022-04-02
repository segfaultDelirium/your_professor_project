import { Component, OnInit } from '@angular/core';
import {GraphqlService} from "../../core/services/graphql.service";
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-countries',
  templateUrl: './countries.component.html',
  styleUrls: ['./countries.component.scss']
})
export class CountriesComponent implements OnInit {
  results: any;

  constructor(public graphqlService: GraphqlService) {}
  ngOnInit(): void {
    this.query();
  }

  query(){
    console.log(this.graphqlService.checkCors().subscribe( res =>{
      console.log(res);
    }))
    // let query = `
    //       {
    //         allCountries{
    //           local_language_name
    //         }
    //       }
    //   `;
    // // console.log(query);
    // // console.log(JSON.stringify(query));
    // let subscription = this.graphqlService.query({
    //   query: `
    //       {
    //         allCountries{
    //           local_language_name
    //         }
    //       }
    //   `
    // }).subscribe( results => {
    //   this.results = results;
    // });
    // console.log(this.results);
  }

}
