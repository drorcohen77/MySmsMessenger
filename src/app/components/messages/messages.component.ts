import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { Message } from 'src/app/Models/message';
import { MessageService } from 'src/app/services/message.service';

@Component({
  selector: 'app-messages',
  templateUrl: './messages.component.html',
  styleUrls: ['./messages.component.css']
})
export class MessagesComponent implements OnInit{

  messages$: Observable<Message[]> = this.taskService.messages;
  messageNum: number = 0;
  
  constructor(private taskService: MessageService) {}

  ngOnInit() { 
    this.taskService.getMessages().subscribe();
  }

  newMessage(message: Message) {
    this.taskService
      .addMessages(message)
      .subscribe();
  }
}
