import { Component } from '@angular/core';
import { CurrenciesService } from './currencies.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  currencies: string[] = [];
  title = 'angular';
  constructor(private currenciesService: CurrenciesService) {}
  ngOnInit(): void {
    this.currenciesService.getCurrencies().subscribe((data) => {
      this.currencies = data['currencies'];
    });
  }
}
