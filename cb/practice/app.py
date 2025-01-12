from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return 'Chatbot is running!'

responses = {
    'greeting': ['Hello!', 'Hi there!', 'Hey!'],
    'farewell': ['Goodbye!', 'See you later!', 'Take care!'],
    'default': ['I did not understand that.', 'Can you please rephrase?', 'I am still learning.'],
}

def get_response(intent):
    return random.choice(responses.get(intent, responses['default']))

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    user_message = data['message']
    
    # Add logic to determine user intent based on user_message
    # For simplicity, let's assume the entire message is the intent for now
    user_intent = user_message.lower()

    bot_response = get_response(user_intent)
    
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True, port=12345)
    
