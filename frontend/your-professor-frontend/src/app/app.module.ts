import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {SignUpModule} from "./auth/sign-up/sign-up.module";
import {LoginModule} from "./auth/login/login.module";
import {ApolloModule, APOLLO_OPTIONS} from "apollo-angular";
import { HttpLink } from 'apollo-angular/http';
import {InMemoryCache} from "@apollo/client/core";
import {HttpClientModule} from "@angular/common/http";

import {LayoutModule} from './layout/layout.module';
import {MaterialModule} from "./core/modules/material/material.module";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import { ExampleQueriesComponent } from './modules/example-queries/example-queries.component';
import { CountriesComponent } from './modules/countries/countries.component';
import { SearchCountryComponent } from './modules/countries/search-country/search-country.component';
import { ListCountriesComponent } from './modules/countries/list-countries/list-countries.component';
import { UpdateCountryComponent } from './modules/countries/update-country/update-country.component';
import { CreateCountryComponent } from './modules/countries/create-country/create-country.component';

@NgModule({
  declarations: [
    AppComponent,
    ExampleQueriesComponent,
    CountriesComponent,
    SearchCountryComponent,
    ListCountriesComponent,
    UpdateCountryComponent,
    CreateCountryComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    LoginModule,
    SignUpModule,
    HttpClientModule,
    LayoutModule,
    MaterialModule,
    FormsModule,
    ReactiveFormsModule,
    ApolloModule,
  ],
  providers: [
    {
      provide: APOLLO_OPTIONS,
      useFactory: (httpLink: HttpLink) =>{
        return {
          cache: new InMemoryCache(),
          link: httpLink.create({
            uri: 'http://localhost:7777/graphql/',
          })
        }
      },
      deps: [HttpLink]
    }
  ],
  bootstrap: [AppComponent, ]
})
export class AppModule { }
