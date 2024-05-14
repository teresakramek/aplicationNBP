import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
// export class LoginComponent implements OnInit {

//   constructor() { }

//   ngOnInit(): void {
//   }

// }

export class LoginComponent {
  username: string = '';
  password: string = '';

  onSubmit(): void {
    console.log(`Username: ${this.username}, Password: ${this.password}`);
  }
}
