
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackAdapter:
    def __init__(self, bot_token):
        self.client = WebClient(token=bot_token)

    def send_message(self, channel_id, message):
        try:
            response = self.client.chat_postMessage(
                channel=channel_id,
                text=message
            )
            return response
        except SlackApiError as e:
            print(f"Error sending message: {e.response['error']}")

    def receive_message(self, request):
        data = request.json
        event = data.get('event', {})
        message = event.get('text')
        channel_id = event.get('channel')
        return channel_id, message
