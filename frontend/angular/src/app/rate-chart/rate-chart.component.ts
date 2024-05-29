import { Component, OnInit, Input, OnChanges } from '@angular/core';
import { Chart } from 'chart.js/auto';
import { Rate } from './../rate.service';

@Component({
  selector: 'app-rate-chart',
  templateUrl: './rate-chart.component.html',
  styleUrls: ['./rate-chart.component.css']
})
export class RateChartComponent implements OnChanges {

  // add interface to the response
  @Input() rates: Array<Rate>  = []

  chart: any = null

  constructor() {}

  ngOnChanges(): void {
    console.log('method on chart component')

    if (this.chart) {
      console.log(this.chart.destroy())
    }

    this.chart = new Chart('canvas', {
      type: 'line',
      data: {
        labels: this.rates.map((rate: Rate) => rate.date),
        datasets: [
          {
            label: 'Rates',
            data: this.rates.map((rate: Rate) => rate.rate),
            borderWidth: 1,
          },
        ],
      },
    });

    console.log(this.chart)
  }

}
