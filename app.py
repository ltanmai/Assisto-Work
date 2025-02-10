from flask import Flask, request
import requests
import logging

app = Flask(__name__)

VERIFY_TOKEN = "hello"
ACCESS_TOKEN = ""

FB_API_URL = "https://graph.facebook.com/v12.0/me/messages"

def verify_webhook():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Verification failed!"

def send_message(recipient_id, message_text):
    data = {
        "recipient": {"id": recipient_id},
        "message": {"text": message_text},
    }
    params = {"access_token": ACCESS_TOKEN}
    response = requests.post(FB_API_URL, json=data, params=params)
    return response.json()

@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return verify_webhook()
    elif request.method == "POST":
        data = request.get_json()
        # print(data)
        if data["object"] == "page":
            for entry in data["entry"]:
                # print()
                # print(entry)
                for messaging_event in entry["messaging"]:
                    # print(messaging_event)
                    # print()
                    if messaging_event.get("message"):
                        sender_id = messaging_event["sender"]["id"]
                        message_text = messaging_event["message"]["text"]
                        # try:
                        #     print(message_text)
                        # except:
                        #     print('failed')
                        logging.warning(data)
                        send_message(sender_id, "Echo: " + message_text)
        return "Message Processed!"

if __name__ == "__main__":
    app.run(port=1234,debug=True)
