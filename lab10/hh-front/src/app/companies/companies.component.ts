import {Component, OnInit} from '@angular/core';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {RouterModule} from "@angular/router";
import {CommonModule, NgForOf, NgIf} from "@angular/common";

import {HHService} from "../hh.service";
import { Company} from '../models';


@Component({
  selector: 'app-companies',
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
  templateUrl: './companies.component.html',
  styleUrl: './companies.component.css'
})
export class CompaniesComponent implements OnInit{
  companies!:Company[];
  loaded:boolean=false
  newCompany:Company;

  constructor(private hhService:HHService)  {
    this.newCompany = {
      "id":0,
      "name":"",
      "description":"",
      "city":"",
      "address":""
    }

  }

  ngOnInit(): void {
    this.getCompanies()
  }
  getCompanies(){
    this.loaded=false;
    this.hhService.getCompanies().subscribe(companies=>this.companies=companies);
    this.loaded=true;
  }
  DeleteCompany(id :number){
    this.hhService.deleteCompany(id).subscribe(()=>{  this.companies = this.companies.filter(company => company.id !== id);
    })
  }
  CreateCompany(){
    const maxId = Math.max(...this.companies.map(company => company.id), 0);
    var copy:Company={
      id:maxId+1,
      name:this.newCompany.name,
      description:this.newCompany.description,
      city:this.newCompany.city,
      address:this.newCompany.address
    };

    this.hhService.postCompany(this.newCompany).subscribe((comp)=>    this.companies.unshift(comp))
    this.newCompany.name='';
    this.newCompany.description='';
    this.newCompany.city='';
    this.newCompany.address='';
  }




}
