import { Component } from '@angular/core';
import { AuthService } from '../auth.service'

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent {
  username: string = '';
  password: string = '';
  errorMessage: string = ''


  constructor(private authService: AuthService) {}

  login(username: string, password: string) {
    this.authService.login(username, password).subscribe(
      (response) => {
        console.log(response)
        console.log('Login successfull');
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
