import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';


export interface Rate {
  date: string,
  rate: Float32Array,
}

@Injectable({
  providedIn: 'root'
})
export class RateService {
  url = 'http://localhost:8000/api/rates/';

  constructor(private http: HttpClient) { }

  getRate(currency:string, date_from:string, date_to: string): Observable<any> {
    let params = new HttpParams().set("date_from", date_from).set("date_to", date_to);
    return this.http.get<Rate>(`${this.url}${currency}`, { params: params });
  }
}
