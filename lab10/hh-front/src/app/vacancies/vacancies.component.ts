import {Component, OnInit} from '@angular/core';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {RouterModule} from "@angular/router";
import {CommonModule, NgForOf, NgIf} from "@angular/common";

import {HHService} from "../hh.service";
import {Company, Vacancy} from '../models';


@Component({
  selector: 'app-vacancies',
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
  templateUrl: './vacancies.component.html',
  styleUrl: './vacancies.component.css'
})
export class VacanciesComponent implements OnInit{
  vacancies!:Vacancy[];
  loaded:boolean=false
  newVacancy:Vacancy;

  constructor(private hhService:HHService) {
    this.newVacancy = {
      "id":0,
      "name":"",
      "description":"",
      "salary":0,
      "Company":{
        "id":0,
        "name":"",
        "description":"",
        "city":"",
        "address":""
      }
    }
  }
  ngOnInit(): void {
    this.getVacancies()
  }
  getVacancies(){
    this.loaded=false;
    this.hhService.getVacancies().subscribe(vac=>this.vacancies=vac);
    this.loaded=true;
  }
  DeleteVacancy(id :number){
    this.hhService.deleteVacancy(id).subscribe(()=>{  this.vacancies = this.vacancies.filter(vac => vac.id !== id);
    })
  }
  CreateVacancy() {
    const maxId = Math.max(...this.vacancies.map(vacancy => vacancy.id), 0);
    var copy: Vacancy = {
      id: maxId + 1,
      name: this.newVacancy.name,
      description: this.newVacancy.description,
      salary: this.newVacancy.salary,
      Company: {
        id: 0,
        name: "",
        description: "",
        city: '',
        address: ''
      }
    };
    this.hhService.getCompany(this.newVacancy.Company.id).subscribe(com => {
      copy.Company = com; // Assign the retrieved company to the copy

      // After getting the company information, post the vacancy
      this.hhService.postVacancy(copy).subscribe((vaca) => {
        this.vacancies.unshift(vaca); // Add the newly created vacancy to the list

        // Clear the form fields
        this.newVacancy.name = '';
        this.newVacancy.description = '';
        this.newVacancy.salary = 0;
        this.newVacancy.Company.id = 0;
      });
    });
  }
}
