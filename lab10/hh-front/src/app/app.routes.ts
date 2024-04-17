import { Routes } from '@angular/router';
import {HomeComponent} from "./home/home.component";
import {AboutComponent} from "./about/about.component";
import {CompaniesComponent} from "./companies/companies.component";
import {VacanciesByCompaniesComponent} from "./vacancies-by-companies/vacancies-by-companies.component";
import {VacanciesComponent} from "./vacancies/vacancies.component";
import {NotFoundComponent} from "./not-found/not-found.component";

export const routes: Routes = [
  { path:"",redirectTo:"home",pathMatch:"full" },
  { path:"home",component:HomeComponent,title:"Home page" },
  { path:"about",component:AboutComponent,title:"About page" },
  { path:"companies",component:CompaniesComponent,title:"Companies page" },
  { path:"companies/:companyId/vacancies", component:VacanciesByCompaniesComponent,
    title:"Vacancies by company page" },
  { path:"vacancies",component:VacanciesComponent,title:"Vacancies page" },
  { path:"**",component:NotFoundComponent,title:"404 - not found" }
];
