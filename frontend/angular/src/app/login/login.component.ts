import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent {
  username: string = '';
  password: string = '';


  constructor() {
    console.log('testing')
  }

  onSubmit(): void {
    console.log(`Username: ${this.username}, Password: ${this.password}`);
  }
}
