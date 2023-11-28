import { Component, OnInit } from '@angular/core'
import { CommonModule } from '@angular/common'
import { ActivatedRoute, Router } from '@angular/router'
import { ButtonModule } from 'primeng/button'
import { CardModule } from 'primeng/card'
import { DayService } from '../day.service'

@Component({
  selector: 'app-day-details',
  standalone: true,
  imports: [CommonModule, ButtonModule, CardModule],
  templateUrl: './day-details.component.html',
  styleUrl: './day-details.component.css',
})
export class DayDetailsComponent implements OnInit {
  day!: number

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private dayService: DayService
  ) {}

  ngOnInit(): void {
    this.day = parseInt(this.route.snapshot.params['day'])
    const day = this.dayService.getDay(this.day)
    console.log(this.day, day)
  }

  back() {
    this.router.navigate(['/day-list'])
  }
}
