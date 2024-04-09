import { Component } from '@angular/core';
import { HttpClient } from '@angular/common'

@Component({
  selector: 'app-app',
  standalone: true,
  imports: [],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  constructor(private http: HttpClient){
  }
  obj:any;
  ngOnInit():void {
    this.obj = this.http.get("http://127.0.0.1:8000/").subscribe{
    data => this.obj = data
    }
  }

}
