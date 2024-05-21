
import requests

class FacebookAdapter:
    def __init__(self, access_token):
        self.access_token = access_token

    def send_message(self, recipient_id, message):
        url = f"https://graph.facebook.com/v10.0/me/messages?access_token={self.access_token}"
        headers = {"Content-Type": "application/json"}
        data = {
            "recipient": {"id": recipient_id},
            "message": {"text": message}
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()

    def receive_message(self, request):
        data = request.json
        message = data['entry'][0]['messaging'][0]['message']['text']
        sender_id = data['entry'][0]['messaging'][0]['sender']['id']
        return sender_id, message
