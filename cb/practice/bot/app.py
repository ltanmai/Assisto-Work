from flask import Flask, render_template, request, jsonify
import nltk
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

# Define chatbot rules
pairs = [
    [
        r"hi|hello",
        ["Hi there! How can I help you?", "Hello! What can I do for you today?"]
    ],
    [
        r"how are you",
        ["I'm doing well, thank you!", "I'm fine, thanks. How about you?"]
    ],
    [
        r"quit|exit",
        ["Goodbye!", "It was nice chatting with you. Have a great day!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand. Can you please rephrase that?", "I'm still learning. Could you ask me something else?"]
    ]
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle chatbot interactions
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']
    chat_response = chatbot.respond(user_message)
    return jsonify({'bot_response': chat_response})

if __name__ == '__main__':
    nltk.download('punkt')  # Download NLTK data for tokenization
    app.run(debug=True, port=1234)
