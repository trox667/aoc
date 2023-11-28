import { Component } from '@angular/core'
import { CommonModule } from '@angular/common'
import { RouterOutlet } from '@angular/router'
import { CardModule } from 'primeng/card'
import { ToolbarModule } from 'primeng/toolbar'
import { DayListComponent } from './day-list/day-list.component'

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule,
    CardModule,
    ToolbarModule,
    RouterOutlet,
    DayListComponent,
  ],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'webui'
}
