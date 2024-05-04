import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RateService {
  url = 'http://localhost:8000/api/rates/';

  constructor(private http: HttpClient) { }

  getRate(currency:string, date_from:string): Observable<any> {
    let params = new HttpParams().set("date_from", date_from);
    return this.http.get(`${this.url}${currency}`, { params: params });
  }
}
