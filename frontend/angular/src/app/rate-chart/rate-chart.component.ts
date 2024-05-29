import { Component, OnInit, Input, OnChanges } from '@angular/core';
import { Chart } from 'chart.js/auto';
import { Rate } from './../rate.service';

@Component({
  selector: 'app-rate-chart',
  templateUrl: './rate-chart.component.html',
  styleUrls: ['./rate-chart.component.css']
})
export class RateChartComponent implements OnChanges {

  @Input() rates: Array<Rate> = []

  chart: any = null

  constructor() {}

  ngOnChanges(): void {

    if (this.chart) {
      this.chart.destroy()
    }

    if (this.rates.length) {
      this.chart = new Chart('canvas', {
        type: 'line',
        data: {
          labels: this.rates.map((rate: Rate) => rate.date),
          datasets: [
            {
              label: '',
              data: this.rates.map((rate: Rate) => rate.rate),
              borderWidth: 1,
            },
          ],
        },
      });
    }
  }
}
