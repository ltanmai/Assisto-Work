from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

VERIFY_TOKEN = 'hello'

@app.route('/')
def home():
    
    access_token = 'EAAFVJxB4ILQBOzrAZCl9LDGAYYYmZCkr3ZB4OVuQvzsssnRZA6dZA5XxJzMKRilOyQSABlkYpSL4ZC3GRWcmNZBZAe0n5S30vXxZBLlqqSRFoUZBVf0wfN1A5vbc8xhBXVuAsNNWQjzKtnCdDxdPmptRTZBh5B3cEDX3CRrtVFZBAPueujsABlit5Jz9u2Y0RdnMQ9uSlfHChSUB'
    page_id = '161674797039606'
    
    api_url = f'https://graph.facebook.com/v18.0/{page_id}/conversations?access_token={access_token}'
    if request.method == 'GET':
        token_sent = request.args.get('hub.verify_token')
        return verify_fb_token(token_sent)
    else:
        try:
            response = requests.get(api_url)
            data = response.json()
            messages = data['data'][0]['messages']['data']

            formatted_messages = [message['message'] for message in messages]   
            return jsonify({'messages': formatted_messages})
        except Exception as e:
            return jsonify({'error': str(e)})

def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

if __name__ == '__main__':
    app.run(debug=True, port=1234)
