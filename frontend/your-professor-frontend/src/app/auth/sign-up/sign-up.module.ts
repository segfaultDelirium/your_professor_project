import {NgModule} from '@angular/core';
import { CommonModule } from '@angular/common';
import { SignUpComponent } from './sign-up.component';
import {AuthModule} from "../auth.module";
import {MatButtonModule} from "@angular/material/button";



@NgModule({
  declarations: [
    SignUpComponent
  ],
  imports: [
    CommonModule,
    AuthModule,
    MatButtonModule
  ]
})
export class SignUpModule { }
