import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AddService {

  constructor(private http: HttpClient) { }

  add(something: string) {
    return this.http.post('https://73xrr9kwd7.execute-api.eu-central-1.amazonaws.com/add', { something }, { responseType: 'text' });
  }
}
