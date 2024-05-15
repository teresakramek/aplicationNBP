import { Component } from '@angular/core';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent{

  username: string = '';
  password: string = '';
  email: string = ''

  constructor() { 
    console.log('testing')
  }

  onSubmit(): void {
    console.log(`Username: ${this.username}, Password: ${this.password}`);
  }

}
