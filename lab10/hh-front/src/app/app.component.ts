import { Component } from '@angular/core';
import {RouterModule, RouterOutlet} from '@angular/router';
import {HomeComponent} from "./home/home.component";
import {AboutComponent} from "./about/about.component";
import {VacanciesComponent} from "./vacancies/vacancies.component";
import {CompaniesComponent} from "./companies/companies.component";
import {NotFoundComponent} from "./not-found/not-found.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterModule, HomeComponent, AboutComponent, VacanciesComponent, CompaniesComponent, VacanciesComponent, NotFoundComponent, RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'hh-front';
}
