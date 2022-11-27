import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable, tap } from 'rxjs';
import { Message } from '../Models/message';

@Injectable({
  providedIn: 'root'
})
export class MessageService {

  private apiUrl = 'http://127.0.0.1:5000';

  private messagesList: Message[] = [];
  private readonly messages$ = new BehaviorSubject<Message[]>([]);
  readonly messages = this.messages$.asObservable();

  constructor(private http: HttpClient) { }

  getMessages(): Observable<Message[]> {
    return this.http.get<Message[]>(this.apiUrl+'/messages')
      .pipe(
        tap(messages => {
          this.messagesList = messages;
          this.messages$.next(this.messagesList);
        })
      );
  }

  addMessages(message: Message): Observable<Message> {

    return this.http.post<Message>(this.apiUrl+'/add_message', message)
      .pipe(
        tap(() => {
          this.messagesList.push(message);
          this.messages$.next(this.messagesList);
        })
      );
  }
}
