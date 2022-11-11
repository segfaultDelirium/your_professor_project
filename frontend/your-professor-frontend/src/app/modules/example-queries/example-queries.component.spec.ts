import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ExampleQueriesComponent } from './example-queries.component';

describe('ExampleQueriesComponent', () => {
  let component: ExampleQueriesComponent;
  let fixture: ComponentFixture<ExampleQueriesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ExampleQueriesComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ExampleQueriesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
