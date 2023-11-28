import { Injectable, Signal } from '@angular/core'
import { toSignal } from '@angular/core/rxjs-interop'
import { of } from 'rxjs'
import { Day } from './Day'

const DAYS: Day[] = [
  {
    day: 1,
    partOne: true,
    partTwo: true,
  },
  {
    day: 2,
    partOne: true,
    partTwo: false,
  },
  {
    day: 3,
    partOne: false,
    partTwo: true,
  },
  {
    day: 4,
    partOne: false,
    partTwo: false,
  },
]

@Injectable({
  providedIn: 'root',
})
export class DayService {
  constructor() {}

  getDays(): Signal<Day[] | undefined> {
    return toSignal(of(DAYS))
  }

  getDay(day: number): Day | undefined {
    return DAYS.find((d) => d.day === day)
  }
}
