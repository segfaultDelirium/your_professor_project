import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './header.component';
import {MaterialModule} from "../../../core/modules/material/material.module";
import {RouterModule} from "@angular/router";


@NgModule({
  declarations: [
    HeaderComponent,
  ],
  imports: [
    CommonModule,
    MaterialModule,
    RouterModule,
  ],
  exports: [
    HeaderComponent,
  ]
})
export class HeaderModule { }
