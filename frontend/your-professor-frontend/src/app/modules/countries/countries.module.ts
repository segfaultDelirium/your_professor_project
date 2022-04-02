import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { CountriesRoutingModule } from './countries-routing.module';
import { CountriesComponent } from './countries.component';
import {GraphqlService} from "../../core/services/graphql.service";



@NgModule({
  declarations: [
    CountriesComponent
  ],
  imports: [
    CommonModule,
    CountriesRoutingModule
  ],
  providers: [
    GraphqlService
  ]
})
export class CountriesModule { }
