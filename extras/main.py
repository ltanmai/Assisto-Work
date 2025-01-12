from flask import Flask, jsonify, abort, request
%store -r forecast
# create an instance of the flask app
app = Flask(__name__)

"""@app.route('/')
def say_hello():
    return 'Hello, World!'"""


'''@app.route("/forecast", methods=["POST"])
def get_forecast():

    if not request.json or not 'days' in request.json:
        predictions = forecast()
    else:
        predictions = forecast(request.json['days'])

    if not predictions:
        abort(400, "Model not found.")

    return jsonify({"forecast": predictions})'''

@app.route("/", methods=["POST"])
def get_forecast():
    return forecast
    

if __name__ == "__main__":
    app.run(debug=True)