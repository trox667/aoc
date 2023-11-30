import { Injectable, Signal } from '@angular/core'
import { toSignal } from '@angular/core/rxjs-interop'
import { of } from 'rxjs'
import { Day } from './Day'
import { HttpClient } from '@angular/common/http'

const DAYS: Day[] = [
  {
    day: 1,
    partOne: 1,
    partTwo: undefined,
  },
  {
    day: 2,
    partOne: undefined,
    partTwo: undefined,
  },
  {
    day: 3,
    partOne: undefined,
    partTwo: undefined,
  },
  {
    day: 4,
    partOne: undefined,
    partTwo: undefined,
  },
]

export interface Solution {
  part: string
  error: string
}

@Injectable({
  providedIn: 'root',
})
export class DayService {
  constructor(private http: HttpClient) {}

  getDays(): Signal<Day[] | undefined> {
    return toSignal(of(DAYS))
  }

  getDay(day: number): Day | undefined {
    return DAYS.find((d) => d.day === day)
  }

  getSolution(day: number, part: number): Signal<Solution | undefined> {
    return toSignal(this.http.get<Solution>(`${URL}/solution/${day}/${part}`))
  }
}
