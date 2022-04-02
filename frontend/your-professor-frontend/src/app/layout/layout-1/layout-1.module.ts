import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {HeaderModule} from "../components/header/header.module";
import {SidebarModule} from "../components/sidebar/sidebar.module";



@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    HeaderModule,
    SidebarModule,
  ],
  exports: [
    HeaderModule,
    SidebarModule,
  ]
})
export class Layout1Module { }
