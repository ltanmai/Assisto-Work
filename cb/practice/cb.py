from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new ChatBot instance
chatbot = ChatBot('SimpleBot')

# Create a ListTrainer for the chatbot
trainer = ListTrainer(chatbot)

# Training the chatbot with a list of conversation pairs
trainer.train([
    'Hi',
    'Hello, how can I assist you?',
    'What is your name?',
    'I am a bot created with ChatterBot.',
    'How are you?',
    'I am just a computer program, but thanks for asking!',
    'Tell me a joke',
    'Why don\'t scientists trust atoms? Because they make up everything!',
    'Goodbye',
    'Goodbye! If you have more questions, feel free to ask.'
])
# Greetings

trainer.train([
    "Hi",
    "Hello, how may I help you?",
])

# Services
    
trainer.train([    
    "I would like to book an appointment with the ENT today",
    "Sure, please choose a slot between Morning, Afternoon, or Evening: ",
    "Afternoon",
    "Your appointment is confirmed. You can come between 12:00 and 16:00.",
    "Morning",
    "Your appointment is confirmed. You can come between 8:00 and 12:00.",
    "Evening",
    "Your appointment is confirmed. You can come between 16:00 and 20:00.",
])


trainer.train([
    "I want to cancel my appointment.",
    "Okay, Your appointment has been cancelled.",
])

trainer.train([
    "I would like to change my appointment slot.",
    "Sure, what slot would you like? You can choose between Morning, afternoon, and Night.",
    "Afternoon",
    "Your appointment is confirmed. Your slot is now between 12:00 and 16:00.",
    "Morning",
    "Your appointment is confirmed. Your slot is now between 8:00 and 12:00.",
    "Evening",
    "Your appointment is confirmed. Your slot is now between 16:00 and 20:00.",
])

trainer.train([
    "What is your phone number? How do I reach you? How do I contact you? How do I call you?",
    "Our number is 01**23**45",
    "What is your address? Where are you located?",
    "You can find us at No. 45, 8th Cross, Oakwood Street",
])

trainer.train([
    "Which Doctor is available?",
    "We have Dr. Esther, Dr. Judith, Dr. Sarah, Dr. Matthew, and Dr. Rob",
    "I want an appointment with Dr. Esther or Dr. Judith or Dr. Sarah or Dr. Matthew or Dr. Rob",
    "Sure, please select your slot",
    "Afternoon",
    "Your appointment is confirmed. You can come between 12:00 and 16:00.",
    "Morning",
    "Your appointment is confirmed. You can come between 8:00 and 12:00.",
    "Evening",
    "Your appointment is confirmed. You can come between 16:00 and 20:00.",
])


# Conclusion

trainer.train([
    "Thank you!",
    "You're most welcome!",
    "Thanks!",
    "Of course!",
    ])


response = chatbot.get_response('Which doctor is available?')

print("Bot Response:", response)