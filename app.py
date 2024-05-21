
from flask import Flask, request, jsonify
from rasa.core.agent import Agent
from facebook_adapter import FacebookAdapter
from whatsapp_adapter import WhatsAppAdapter
from slack_adapter import SlackAdapter
from plugin_loader import PluginLoader

app = Flask(__name__)
agent = Agent.load("models/nlu")
facebook_adapter = FacebookAdapter("YOUR_FACEBOOK_PAGE_ACCESS_TOKEN")
whatsapp_adapter = WhatsAppAdapter("TWILIO_ACCOUNT_SID", "TWILIO_AUTH_TOKEN", "YOUR_WHATSAPP_NUMBER")
slack_adapter = SlackAdapter("YOUR_SLACK_BOT_TOKEN")
plugin_loader = PluginLoader()

plugin_loader.load_plugins()

@app.route("/webhook/facebook", methods=["POST"])
def facebook_webhook():
    sender_id, message = facebook_adapter.receive_message(request)
    response = plugin_loader.handle_message(message)
    facebook_adapter.send_message(sender_id, response)
    return jsonify({"status": "success"})

@app.route("/webhook/whatsapp", methods=["POST"])
def whatsapp_webhook():
    sender_id, message = whatsapp_adapter.receive_message(request)
    response = plugin_loader.handle_message(message)
    whatsapp_adapter.send_message(sender_id, response)
    return jsonify({"status": "success"})

@app.route("/webhook/slack", methods=["POST"])
def slack_webhook():
    channel_id, message = slack_adapter.receive_message(request)
    response = plugin_loader.handle_message(message)
    slack_adapter.send_message(channel_id, response)
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(port=5005)
