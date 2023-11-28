import { Routes } from '@angular/router';
import { DayListComponent } from './day-list/day-list.component';
import { DayDetailsComponent } from './day-details/day-details.component';

export const routes: Routes = [
  {
    path: '',
    redirectTo: 'day-list',
    pathMatch: 'full'
  },
  {
    path: 'day-list',
    component: DayListComponent
  },
  {
    path: 'day-detail/:day',
    component: DayDetailsComponent
  }
];
