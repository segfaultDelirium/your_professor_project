import { Component, OnInit } from '@angular/core';
import { Apollo, gql } from 'apollo-angular';

@Component({
  selector: 'app-QueryExecutor',
  templateUrl: './query-executor.component.html',
  styleUrls: ['./query-executor.component.scss']
})
export class QueryExecutorComponent implements OnInit {
  results: any;
  loading = true;
  error: any;
  queryString: string = `
  {
    allCountries{
      local_language_name
    }
  }
`;

  constructor(private apollo: Apollo) { }
  ngOnInit(): void {
    this.query();
  }

  query() {
    let result = this.apollo
      .watchQuery({
        query: gql`
          ${this.queryString}
        `,
      })
      .valueChanges.subscribe((result: any) => {
        this.results = result?.data;
        this.loading = result.loading;
        this.error = result.error;
        console.log(this.results)
      });
  }
  stringify(value: any){
    return JSON.stringify(value, null, 4);
  }
  
}
