import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Company,Vacancy} from "./models";

@Injectable({
  providedIn: 'root'
})
export class HHService {

  constructor(private client:HttpClient) { }
  getCompanies(){
    return this.client.get<Company[]>(`http://127.0.0.1:8000/api/companies/`,)
  }
  getCompany(id:number){
    return this.client.get<Company>(`http://127.0.0.1:8000/api/companies/${id}/`)
  }
  deleteCompany(id:number){
    return this.client.delete(`http://127.0.0.1:8000/api/companies/${id}/`)
  }
  postCompany(newCompany:Company){
    console.log(newCompany.id)

    return this.client.post<Company>(`http://127.0.0.1:8000/api/companies/`,newCompany)
  }
  putCompany(newCompany:Company){
    return this.client.put<Company>(`http://127.0.0.1:8000/api/companies/${newCompany.id}/`,newCompany)
  }

  getVacanciesByCompany(companyId: number) {
    return this.client.get<Vacancy[]>(`http://127.0.0.1:8000/api/companies/${companyId}/vacancies/`)
  }
  getVacancies(){
    return this.client.get<Vacancy[]>(`http://127.0.0.1:8000/api/vacancies/`,)
  }
  getVacancy(id:number){
    return this.client.get<Vacancy>(`http://127.0.0.1:8000/api/vacancies/${id}/`)
  }
  deleteVacancy(id:number){
    return this.client.delete(`http://127.0.0.1:8000/api/vacancies/${id}/`)
  }
  postVacancy(newVacancy:Vacancy){
    return this.client.post<Vacancy>(`http://127.0.0.1:8000/api/vacancies/`,newVacancy)
  }
  putVacancy(newVacancy:Vacancy){
    return this.client.put<Vacancy>(`http://127.0.0.1:8000/api/vacancies/${newVacancy.id}/`,newVacancy)
  }
  getTopTenVacancies(){
    return this.client.get<Vacancy[]>(`http://127.0.0.1:8000/api/vacancies/top_ten/`)
  }
}
