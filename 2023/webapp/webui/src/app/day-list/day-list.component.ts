import { Component, Signal } from '@angular/core'
import { CommonModule } from '@angular/common'
import { Router } from '@angular/router'
import { ButtonModule } from 'primeng/button'
import { DataViewModule } from 'primeng/dataview'

import { DayService } from '../day.service'
import { Day } from '../Day'

@Component({
  selector: 'app-day-list',
  standalone: true,
  imports: [CommonModule, ButtonModule, DataViewModule],
  templateUrl: './day-list.component.html',
  styleUrl: './day-list.component.css',
})
export class DayListComponent {
  protected days: Signal<Day[] | undefined>

  constructor(private router: Router, private dayService: DayService) {
    this.days = dayService.getDays()
  }

  openDay(day: number) {
    console.log('openDay', day)
    this.router.navigate(['/day-detail', day])
  }
}
