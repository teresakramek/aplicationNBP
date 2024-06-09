import { ComponentFixture, TestBed } from '@angular/core/testing';
import { DashboardComponent } from './dashboard.component';
import { CurrenciesService } from '../currencies.service';
import { RateService } from '../rate.service';
import { AuthService } from '../auth.service';
import { RouterTestingModule } from '@angular/router/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { of } from 'rxjs';
import { FormsModule, NgForm } from '@angular/forms';
import { Router } from '@angular/router';

fdescribe('DashboardComponent', () => {
  let component: DashboardComponent;
  let fixture: ComponentFixture<DashboardComponent>;
  let currenciesService: jasmine.SpyObj<CurrenciesService>;
  let rateService: jasmine.SpyObj<RateService>;
  let authService: jasmine.SpyObj<AuthService>;

  beforeEach(async () => {
    const currenciesServiceSpy = jasmine.createSpyObj('CurrenciesService', ['getCurrencies'])
    const rateServiceSpy = jasmine.createSpyObj('RateService', ['getRate']);
    const authServiceSpy = jasmine.createSpyObj('AuthService', ['logout']);

    await TestBed.configureTestingModule({
      imports: [
        HttpClientTestingModule,
        RouterTestingModule,
        FormsModule
      ],
      declarations: [DashboardComponent],
      providers: [
        { provide: CurrenciesService, useValue: currenciesServiceSpy },
        { provide: RateService, useValue: rateServiceSpy },
        { provide: AuthService, useValue: authServiceSpy }
      ]
    }).compileComponents();

    currenciesService = TestBed.inject(CurrenciesService) as jasmine.SpyObj<CurrenciesService>;
    rateService = TestBed.inject(RateService) as jasmine.SpyObj<RateService>;
    authService = TestBed.inject(AuthService) as jasmine.SpyObj<AuthService>;

    currenciesService.getCurrencies.and.returnValue(of({}))
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DashboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should fetch currencies on init', () => {
    const mockCurrencies = { currencies: ['USD', 'EUR', 'GBP'] };
    currenciesService.getCurrencies.and.returnValue(of(mockCurrencies));

    component.ngOnInit();
    fixture.detectChanges();

    expect(currenciesService.getCurrencies).toHaveBeenCalled();
    expect(component.currencies).toEqual(mockCurrencies.currencies);
  });

  it('should fetch rates on form submit', () => {
    const mockRates = { rates: { USD: 1.2, EUR: 1.1 } };
    const form = { value: { currency: 'USD', date_from: '2021-01-01', date_to: '2021-01-31' } } as NgForm;
    rateService.getRate.and.returnValue(of(mockRates));

    component.onSubmit(form);
    fixture.detectChanges();

    expect(rateService.getRate).toHaveBeenCalledWith('USD', '2021-01-01', '2021-01-31');
    expect(component.rates).toEqual(mockRates);
  });

  it('should logout and navigate to home', () => {
    const router = TestBed.inject(Router);
    spyOn(router, 'navigate');

    component.logout();

    expect(authService.logout).toHaveBeenCalled();
    expect(router.navigate).toHaveBeenCalledWith(['']);
  });
});
