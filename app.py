import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__baseball__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def Prediction(pitch_input):
    features = np.array(pitch_input)
    result = model.predict(features)
    return result[0]


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        pitch_input = request.form.to_dict()
        pitch_input = list(pitch_input.values())
        pitch_input = list(map(int, pitch_input))
        result = Prediction(pitch_input)
        if int(result) == 1:
            prediction = 'STEEEEERIKE'
        else:
            prediction = 'BALL (Or Maybe a hit)!'
        return prediction


if __name__ == '__main__':
    app.run(debug=True)