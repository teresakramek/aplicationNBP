import { ComponentFixture, TestBed } from '@angular/core/testing';
import { LoginComponent } from './login.component';
import { AuthService } from '../auth.service';
import { RouterTestingModule } from '@angular/router/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { of, throwError } from 'rxjs';
import { Router } from '@angular/router';

fdescribe('LoginComponent', () => {
  let component: LoginComponent;
  let fixture: ComponentFixture<LoginComponent>;
  let authService: jasmine.SpyObj<AuthService>;
  let router: Router;

  beforeEach(async () => {
    const authServiceSpy = jasmine.createSpyObj('AuthService', ['login']);

    await TestBed.configureTestingModule({
      imports: [
        HttpClientTestingModule,
        RouterTestingModule
      ],
      declarations: [LoginComponent],
      providers: [
        { provide: AuthService, useValue: authServiceSpy }
      ]
    }).compileComponents();

    authService = TestBed.inject(AuthService) as jasmine.SpyObj<AuthService>;
    router = TestBed.inject(Router);
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LoginComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should call AuthService login on login method call and navigate on success', () => {
    const mockResponse = { access_token: 'dummy_token' };
    authService.login.and.returnValue(of(mockResponse));
    const spyNavigate = spyOn(router, 'navigate');

    component.login('testuser', 'testpass');

    expect(authService.login).toHaveBeenCalledWith('testuser', 'testpass');
    expect(localStorage.getItem('token')).toBe('dummy_token');
    expect(spyNavigate).toHaveBeenCalledWith(['dashboard']);
  });

  it('should set error message on login failure with status 401', () => {
    const mockError = { status: 401 };
    authService.login.and.returnValue(throwError(mockError));

    component.login('testuser', 'testpass');

    expect(authService.login).toHaveBeenCalledWith('testuser', 'testpass');
    expect(component.errorMessage).toBe('Incorrect username or password.');
  });

  it('should set error message on login failure with other status', () => {
    const mockError = { status: 500 };
    authService.login.and.returnValue(throwError(mockError));

    component.login('testuser', 'testpass');

    expect(authService.login).toHaveBeenCalledWith('testuser', 'testpass');
    expect(component.errorMessage).toBe('An error occurred. Please try again later.');
  });
});
