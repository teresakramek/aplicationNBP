import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http: HttpClient) { }

  login(username: string, password: string) {
    const body = new HttpParams()
    .set('username', username)
    .set('password', password)
    .toString();

    const headers = new HttpHeaders({
      'Content-Type': 'application/x-www-form-urlencoded'
    });

    return this.http.post<any>('http://localhost:8000/api/login', body, { headers });
  }
  logout() {
    localStorage.removeItem('token');
  }

  register(username: string, email:string, password: string) {
    return this.http.post<any>('http://localhost:8000/api/register', { username: username, email: email, password: password})
  }
}
