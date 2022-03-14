import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {HeaderModule} from "./header/header.module";
import {SignUpModule} from "./auth/sign-up/sign-up.module";
import {LoginModule} from "./auth/login/login.module";
import {APOLLO_OPTIONS} from "apollo-angular";
import { HttpLink } from 'apollo-angular/http';
import {InMemoryCache} from "@apollo/client/core";
import {HttpClientModule} from "@angular/common/http";

@NgModule({
  declarations: [
    AppComponent,

  ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        BrowserAnimationsModule,
        HeaderModule,
        LoginModule,
        SignUpModule,
        HttpClientModule
    ],
  providers: [
    {
      provide: APOLLO_OPTIONS,
      useFactory: (httpList: HttpLink) =>{
        return {
          cache: new InMemoryCache(),
          link: httpList.create({
            uri: 'api/graphql',
          })
        }
      },
      deps: [HttpLink]
    }
  ],
  bootstrap: [AppComponent, ]
})
export class AppModule { }
