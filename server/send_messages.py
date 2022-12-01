import os
from twilio.rest import Client
from dotenv import load_dotenv


load_dotenv('.env')


def send_message(destination: str, message: str):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
          body=message,
          from_='+19148955904',
          to=destination
        )

    print(message.sid)


def main():
    send_message('+972545250514', "Hello from python!")


if __name__ == '__main__':
    main()

