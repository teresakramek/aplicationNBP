import { Component } from '@angular/core';
import { CurrenciesService } from './currencies.service';
import { NgForm } from '@angular/forms';

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

  onSubmit(f: NgForm): void {
    console.log(f.value);
    console.log('Tesia jest super');
  }

}
