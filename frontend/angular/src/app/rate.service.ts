import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RateService {
  url = 'http:/localhost:8000/api/rates/';
  constructor(private http: HttpClient) { }
  getRate(): Observable<any> {
    return this.http.get(this.url);
  }
}
