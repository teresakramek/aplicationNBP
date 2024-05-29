import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { config } from './../../config';

@Injectable({
  providedIn: 'root'
})
export class CurrenciesService {

  constructor(private http: HttpClient) {}
  
  getCurrencies(): Observable<any> {
    return this.http.get(`${config.BACKEND_URL}/api/currencies/`, { headers: { Accept: 'application/json' }});
  }
}
