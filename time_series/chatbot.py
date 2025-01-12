import requests

#check what this function does
def send_message(message):
    response = requests.post('http://localhost:12345/predictions', json={'days': message})
    return response.json()

def chatbot():
    print("Chatbot: Hello! I'm a time series forecasting chatbot. You can ask me to predict temperatures for future days.")
    
    while True:
        user_input = input("User: ")
        
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        try:
            # Assume the user input is the number of days for predictions
            days = int(user_input)
            if days > 0:
                response = send_message(days)
                dates = ', '.join(response['dates'])
                predictions = ', '.join(map(str, response['prediction']))
                date=dates.split(', ')
                prediction=predictions.split(', ')
                print("Chatbot:")
                for i, j in zip(date, prediction):
                    print(f"Predicted date: {i}, Prediction: {j}")

            else:
                print("Chatbot: Please provide a valid positive number of days for predictions.")
        except ValueError:
            print("Chatbot: I'm sorry, I didn't understand that. Please provide a valid number of days or type 'exit' to end the conversation.")

if __name__ == '__main__':
    chatbot()
