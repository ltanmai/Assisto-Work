from flask import Flask, request
import requests
import logging

app = Flask(__name__)

Verify_token = 'hello'
Access_token ='EAAFVJxB4ILQBOwyUlUsdcdGBriLYAxW3YVAWVp4bo8cQ4wiDJxMXhJl1WtrI0vMcCijO9Pt4HfXsaq8xx191bYr8UfsqmTXfIdbxaKHx5ZCsbM5KKKyjkpkyhkUE50s7odltEavS2YPA3B358rUZCFX4ZCCBJQnIluGxZAUcYEt2JLYyttAac61jcaFRPZAFcq7z53dZC3'

fb_api_url='https://graph.facebook.com/v12.0/me/messages'

def verify_webhook():
    if request.args.get("hub.verify_token")==Verify_token:
        return request.args.get("hub.challenge")
    return "Verification failed!"

def send_message(recipient_id, message_text):
    data={
        "recipient":{"id":recipient_id},
        "message":{"text":message_text}
    }
    params={"access_token":Access_token}
    response=requests.post(fb_api_url, json=data, params=params)
    return response.json

@app.route('/', methods=['GET','POST'])
def webhook():
    if request.method=="GET":
        return verify_webhook()
    elif request.method=="POST":
        data=request.get_json()
        if data["object"] == "page":
            for entry in data["entry"]:
                for messaging_event in entry["messaging"]:
                    if messaging_event.get("message"):
                        sender_id = messaging_event["sender"]["id"]
                        message_text = messaging_event["message"]["text"]
                        send_message(sender_id, "Bot: " + message_text)
        return "Message Processed"

if __name__=="__main__":
    app.run(port=1234, debug=True)