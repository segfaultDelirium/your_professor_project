import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { MatToolbarModule} from "@angular/material/toolbar";
import { MatIconModule} from "@angular/material/icon";
import { MatSliderModule} from "@angular/material/slider";
import { MatButtonModule} from "@angular/material/button";
import {MatSlideToggleModule} from "@angular/material/slide-toggle";
import {MatSidenavModule} from "@angular/material/sidenav";
import {MatDividerModule} from "@angular/material/divider";
import {MatListModule} from "@angular/material/list";
import {MatGridListModule} from "@angular/material/grid-list";
import {MatCardModule} from "@angular/material/card";
import {MatCheckboxModule} from "@angular/material/checkbox";

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    MatToolbarModule,
    MatIconModule,
    MatSliderModule,
    MatButtonModule,
    MatSlideToggleModule,
    MatSidenavModule,
    MatDividerModule,
    MatListModule,
    MatGridListModule,
    MatCardModule,
    MatCheckboxModule,
  ],
  exports: [
    MatToolbarModule,
    MatIconModule,
    MatSliderModule,
    MatButtonModule,
    MatSlideToggleModule,
    MatSidenavModule,
    MatDividerModule,
    MatListModule,
    MatGridListModule,
    MatCardModule,
    MatCheckboxModule,
  ]
})
export class MaterialModule { }
