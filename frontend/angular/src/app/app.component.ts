import { Component } from '@angular/core';
import { CurrenciesService } from './currencies.service';
import { NgForm } from '@angular/forms';
import { RateService } from './rate.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  currencies: string[] = [];
  title = 'angular';

  constructor(private currenciesService: CurrenciesService, private rateService: RateService) {}

  ngOnInit(): void {
    this.currenciesService.getCurrencies().subscribe((data) => {
      this.currencies = data['currencies'];
    });
  }

  onSubmit(f: NgForm): void {
    console.log(f.value);
    console.log('Teresa - dasz radę');
    const result = this.rateService.getRate(f.value.currency, f.value.date_from).subscribe((data) => {
      console.log(data)
    });
  }

}
