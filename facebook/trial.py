from flask import Flask, request

app = Flask(__name__)
ACCESS_TOKEN = 'EAAFVJxB4ILQBOzVGqpTN5gBzUtgLGKCsVdOg2W2SmQqHjcrs7470VoluK3p5ZBYKF3FExBUCQYq64ci83JKbBjnJtjjNy5iMoOvYdSYug1eCE60XpM247CA3umOF3nb9TJZCah5WjxRiB0lLqlHmXSOjQ0TnsBlzdX5ZBnnB5yuozSPHXKYawNGlGrpZBpwEC0T2QpAu'
VERIFY_TOKEN = 'hello'

@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        token_sent = request.args.get('hub.verify_token')
        return verify_fb_token(token_sent)
    else:
        output = request.get_json()
        for event in output['entry']:
            if 'messaging' in event:
                for message in event['messaging']:
                    if 'message' in message:
                        process_message(message)
        print (output)

def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

def process_message(message):
    sender_id = message['sender']['id']
    recipient_id = message['recipient']['id']
    if 'text' in message['message']:
        text = message['message']['text']
        display_message(sender_id, text)

def display_message(sender_id, text):
    print(f"Received message from user {sender_id}: {text}")

if __name__ == '__main__':
    app.run(debug=True, port=1234)
