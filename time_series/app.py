from flask import Flask, jsonify, request, render_template
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

app = Flask(__name__)

# Load the dataset and train the ARIMA model
df = pd.read_csv('MaunaLoaDailyTemps.csv', index_col='DATE', parse_dates=True).dropna()
model2 = ARIMA(df['AvgTemp'], order=(1, 0, 5)).fit()

@app.route('/')
def home():
    return "hello world"

@app.route('/predictions', methods=['POST'])
def prediction():
    try:
        data = request.get_json()
        days = data.get('days')

        if days is not None:
            pred = model2.predict(start=len(df), end=len(df) + days, typ='levels').rename('ARIMA Predictions')
            index_future_dates = pd.date_range(start='2019-01-30', periods=days+1)

            pred.index = index_future_dates

            return jsonify({'dates': pred.index.strftime('%Y-%m-%d').to_list(),
                            'prediction': pred.to_list()})
        else:
            return jsonify({'error': 'Please provide the number of days for predictions.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=12345)
    