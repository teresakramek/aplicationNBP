import { Component, OnInit } from '@angular/core';
import { CurrenciesService } from '../currencies.service';
import { NgForm } from '@angular/forms';
import { RateService } from '../rate.service';
import { AuthService } from '../auth.service'
import { Router } from '@angular/router';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  currencies: string[] = [];
  rates: any = [];
  title = 'angular';

  constructor(
    private currenciesService: CurrenciesService, 
    private rateService: RateService,
    private authService: AuthService, 
    private router: Router 
  ) {}

  ngOnInit(): void {
    this.currenciesService.getCurrencies().subscribe((data) => {
      this.currencies = data['currencies'];
    });
  }

  onSubmit(f: NgForm): void {
    console.log(f.value);
    console.log('Teresa - dasz radę');
    this.rateService.getRate(f.value.currency, f.value.date_from, f.value.date_to).subscribe((data) => {
      console.log(data)
      this.rates = data;
    });
  }

  logout() {
    console.log('Test')
    this.authService.logout();
    this.router.navigate([''])
  }
}

