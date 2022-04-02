import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {map, Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class GraphqlService {

  constructor(private http: HttpClient) { }

  public checkCors(){
    return this.http.get("localhost:8000");
  }

  public query<T>(options: {
    query: string;
    variables?: { [key: string]: any };
  }): Observable<T> {
    return this.http
      .post<{ data: T }>(`localhost:7777/graphql`, {
        query: options.query,
        variables: options.variables,
      })
      .pipe(map((d) => d.data));
  }

  public mutate<T>(options: {
    mutation: string;
    variables?: { [key: string]: any };
  }): Observable<any> {
    return this.http
      .post<{ data: T }>(`/graphql`, {
        query: options.mutation,
        variables: options.variables,
      })
      .pipe(map((d) => d.data));
  }
}
