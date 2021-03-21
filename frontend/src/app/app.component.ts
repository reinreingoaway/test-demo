import { AddService } from './add.service';
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  constructor(private addService: AddService) {}
  header = 'Add something to the database';
  inputtedData;
  outputResponse;

  submit() {
    this.addService.add(this.inputtedData).subscribe(
      (res) => this.outputResponse = res,
      (err) => this.outputResponse = err.error.text || err.error,
    );
  }
}
