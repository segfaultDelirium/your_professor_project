import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { QueryExecutorRoutingModule } from './query-executor-routing.module';
import { QueryExecutorComponent } from './query-executor.component';
import { MaterialModule } from 'src/app/core/modules/material/material.module';



@NgModule({
  declarations: [
    QueryExecutorComponent
  ],
  imports: [
    CommonModule,
    QueryExecutorRoutingModule,
    MaterialModule
  ],
  providers: [
  ]
})
export class QueryExecutorModule { }
