import { ComponentFixture, TestBed } from '@angular/core/testing';

import { QueryExecutorComponent } from './query-executor.component';

describe('QueryExecutorComponent', () => {
  let component: QueryExecutorComponent;
  let fixture: ComponentFixture<QueryExecutorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ QueryExecutorComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(QueryExecutorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
