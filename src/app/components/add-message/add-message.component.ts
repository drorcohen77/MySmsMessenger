import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { Message } from 'src/app/Models/message';

@Component({
  selector: 'app-add-message',
  templateUrl: './add-message.component.html',
  styleUrls: ['./add-message.component.css']
})
export class AddMessageComponent implements OnInit{
  @Output() onNewMessage = new EventEmitter();
  phoneNumber: string = '';
  message: string = '';

  constructor(){}

  ngOnInit(): void {
    
  }

  onSubmit() {
    const nowDate = new Date().toUTCString();
    const charCount =`${this.message.length}/100` ;
    
    const newMessage = {
      message: this.message,
      phoneNumber: this.phoneNumber,
      time: nowDate,
      charNum: charCount
    }

    this.onNewMessage.emit(newMessage);

    this.message = '';
    this.phoneNumber = '';
  
  }

  clear(){
    this.message = '';
    this.phoneNumber = '';
  }
}
