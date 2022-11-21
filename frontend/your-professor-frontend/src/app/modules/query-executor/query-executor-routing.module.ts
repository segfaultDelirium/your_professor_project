import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { QueryExecutorComponent } from './query-executor.component';

const routes: Routes = [{ path: '', component: QueryExecutorComponent }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class QueryExecutorRoutingModule { }
