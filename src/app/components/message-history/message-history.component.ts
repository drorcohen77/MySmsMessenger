import { Component, Input, OnInit } from '@angular/core';
import { Message } from 'src/app/Models/message';

@Component({
  selector: 'app-message-history',
  templateUrl: './message-history.component.html',
  styleUrls: ['./message-history.component.css']
})
export class MessageHistoryComponent implements OnInit{
  @Input() message!: Message;
  
  constructor(){}

  ngOnInit(): void {}

}
