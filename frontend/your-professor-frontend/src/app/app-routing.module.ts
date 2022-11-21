import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {LoginComponent} from "./auth/login/login.component";
import {SignUpComponent} from "./auth/sign-up/sign-up.component";
import { CountriesComponent } from './modules/countries/countries.component';
import { ExampleQueriesComponent } from './modules/example-queries/example-queries.component';

const routes: Routes = [
  {
    path: 'login', component: LoginComponent
  },
  {
    path: 'signup', component: SignUpComponent
  },
  { path: 'home', loadChildren: () => import('./modules/home/home.module').then(m => m.HomeModule) },
  { path: '', redirectTo: 'home', pathMatch: 'full'},
  { path: 'examples', component: ExampleQueriesComponent},
  { path: 'QueryExecutor', loadChildren: () => import('./modules/query-executor/query-executor.module').then(m => m.QueryExecutorModule) },
  { path: 'countries', component: CountriesComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
