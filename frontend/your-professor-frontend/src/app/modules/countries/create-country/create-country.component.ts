import { Component, OnInit } from '@angular/core';
import { Apollo, gql } from 'apollo-angular';

type NewCountry = {
  ISO_code_name: string,
  local_language_name: string
}

@Component({
  selector: 'app-create-country',
  templateUrl: './create-country.component.html',
  styleUrls: ['./create-country.component.scss']
})
export class CreateCountryComponent implements OnInit {

  newCountry: NewCountry = {
    ISO_code_name: '',
    local_language_name: ''
  }

  constructor(private apollo: Apollo) { }

  ngOnInit(): void {
  }

  result: any;
  loading: any;
  error: string = '';
  status: boolean;


  query(newCountry: NewCountry){

    // mutation UpvotePost($postId: Int!) {
    //   upvotePost(postId: $postId) {
    //     id
    //     votes
    //   }
    // }
    let mutationString = gql`
    mutation createCountryByISO($ISO_code_name: String!, $local_language_name: String!){
      createCountryByISO(ISO_code_name: $ISO_code_name, local_language_name: $local_language_name){
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
    this.apollo
        .mutate({
          
          mutation: mutationString,
          variables: {
            local_language_name: this.newCountry.local_language_name,
            ISO_code_name: this.newCountry.ISO_code_name
          }
          
        })
        .subscribe(
          ({ data }) => {
            let result = data as any;
            console.log(data);
            this.result =  result?.createCountryByISO.country;
            this.error =  result.error;
            this.status =  result.status;
            console.log(this.result)
          },
          error => {
            console.log('there was an error sending the query', error)
          }
        )

      // .valueChanges.subscribe((result: any) => {
      //   console.log(result);
      //   this.result = result?.data.createCountryByISO.country;
      //   this.error = result.createCountryByISO.error;
      //   this.status = result.createCountryByISO.status;
      //   console.log(this.result)
      // });
  }

}
