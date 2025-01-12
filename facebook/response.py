from flask import Flask, request
from jina import Flow, requests, Executor
from docarray import BaseDoc, DocList

app = Flask(__name__)

Verify_token = 'hello'
Access_token ='EAAFVJxB4ILQBOwyUlUsdcdGBriLYAxW3YVAWVp4bo8cQ4wiDJxMXhJl1WtrI0vMcCijO9Pt4HfXsaq8xx191bYr8UfsqmTXfIdbxaKHx5ZCsbM5KKKyjkpkyhkUE50s7odltEavS2YPA3B358rUZCFX4ZCCBJQnIluGxZAUcYEt2JLYyttAac61jcaFRPZAFcq7z53dZC3'
fb_api_url = 'https://graph.facebook.com/v12.0/me/messages'


class res(BaseDoc):
    def __init__(self, recipient_id: str, message_text: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.recipient_id = recipient_id
        self.message_text = message_text

class FacebookMessengerExecutor(Executor):
    @requests(on='/send_message')
    def send_message(self, docs: DocList[res], **kwargs):
        for doc in docs:
            recipient_id = doc.recipient_id
            message_text = doc.message_text
            data = {
                "recipient": {"id": recipient_id},
                "message": {"text": message_text}
            }
            params = {"access_token": Access_token}
            response = requests.post(fb_api_url, json=data, params=params)
            return response.json()


def verify_webhook():
    if request.args.get("hub.verify_token") == Verify_token:
        return request.args.get("hub.challenge")
    return "Verification failed!"


@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == "GET":
        return verify_webhook()
    elif request.method == "POST":
        data = request.get_json()
        if data["object"] == "page":
            for entry in data["entry"]:
                for messaging_event in entry["messaging"]:
                    if messaging_event.get("message"):
                        sender_id = messaging_event["sender"]["id"]
                        message_text = messaging_event["message"]["text"]
                        response = res(sender_id, message_text)
                        docs = DocList()
                        docs.append(response)
                        with Flow(protocol='gRPC', port=5000).add(uses=FacebookMessengerExecutor) as f:
                            f.post(on='/send_message', inputs=docs)

        return "Message Processed"


if __name__ == "__main__":
    app.run(port=1234, debug=True)
