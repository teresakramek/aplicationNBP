import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CurrenciesService {
  url = 'http://localhost:8000/api/currencies';
  constructor(private http: HttpClient) {}
  getCurrencies(): Observable<any> {
    return this.http.get(this.url, { headers: { Accept: 'application/json' }});
  }
}
