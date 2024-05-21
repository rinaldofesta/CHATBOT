
from twilio.rest import Client

class WhatsAppAdapter:
    def __init__(self, account_sid, auth_token, from_number):
        self.client = Client(account_sid, auth_token)
        self.from_number = from_number

    def send_message(self, to_number, message):
        message = self.client.messages.create(
            body=message,
            from_=f'whatsapp:{self.from_number}',
            to=f'whatsapp:{to_number}'
        )
        return message.sid

    def receive_message(self, request):
        message = request.form['Body']
        sender_id = request.form['From']
        return sender_id, message
