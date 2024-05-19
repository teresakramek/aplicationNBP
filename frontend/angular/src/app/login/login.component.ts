import { Component } from '@angular/core';
import { AuthService } from '../auth.service'
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent {
  username: string = '';
  password: string = '';
  errorMessage: string = ''


  constructor(private authService: AuthService, private router: Router) {}

  login(username: string, password: string) {
    this.authService.login(username, password).subscribe(
      (response) => {
        localStorage.setItem('token', response.access_token);
        this.router.navigate(['dashboard'])
      },
      (error) => {
        if (error.status === 401) {
          this.errorMessage = 'Incorrect username or password.';
        } else {
          this.errorMessage = 'An error occurred. Please try again later.';
        }
      }
    )
  }

}
