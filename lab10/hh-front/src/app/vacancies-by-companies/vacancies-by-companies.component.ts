import {Component, OnInit} from '@angular/core';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {ActivatedRoute, RouterModule} from "@angular/router";
import {CommonModule, NgForOf, NgIf} from "@angular/common";

import {HHService} from "../hh.service";
import {Company, Vacancy} from '../models';


@Component({
  selector: 'app-vacancies-by-companies',
  standalone: true,
  imports: [
    ReactiveFormsModule,
    RouterModule,
    FormsModule,
    CommonModule,
    NgForOf,
    NgIf,
    ReactiveFormsModule
  ],
  templateUrl: './vacancies-by-companies.component.html',
  styleUrl: './vacancies-by-companies.component.css'
})
export class VacanciesByCompaniesComponent implements OnInit {
  vacancies!: Vacancy[];
  company!: Company;
  loaded: boolean = false;
  newVacancy: Vacancy;

  constructor(private hhService: HHService, private route: ActivatedRoute) {
    this.newVacancy = {
      id: 0,
      name: "",
      description: "",
      salary: 0,
      Company: {
        id: 0,
        name: "",
        description: "",
        city: "",
        address: ""
      }
    };
  }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      const companyId = params['companyId'];
      this.hhService.getCompany(companyId).subscribe(com => {
        this.company = com;
        this.newVacancy.Company = this.company;
        this.getVacanciesByCompany(this.company.id);
        console.log(this.company.name); // Moved inside the subscription callback
      });
    });
  }

  getVacanciesByCompany(id: number) {
    this.loaded = false;
    this.hhService.getVacanciesByCompany(id).subscribe(vac => {
      this.vacancies = vac;
      this.loaded = true; // Set loaded to true once data is fetched
    });
  }

  DeleteVacancy(id: number) {
    this.hhService.deleteVacancy(id).subscribe(() => {
      this.vacancies = this.vacancies.filter(vac => vac.id !== id);
    });
  }

  CreateVacancy() {
    // Consider fetching maxId more efficiently
    this.hhService.getVacancies().subscribe(vac => {
      const maxId = Math.max(...vac.map(vacancy => vacancy.id), 0);
      const copy: Vacancy = {
        id: maxId + 1,
        name: this.newVacancy.name,
        description: this.newVacancy.description,
        salary: this.newVacancy.salary,
        Company: this.newVacancy.Company
      };

      this.hhService.postVacancy(copy).subscribe((vaca) => {
        this.vacancies.unshift(vaca);
        this.newVacancy.name = '';
        this.newVacancy.description = '';
        this.newVacancy.salary = 0;
      });
    });
  }
}
