import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('all_pitchers_gbc_pitch.sav', 'rb'))

# Home page
@app.route('/')
def home():
    return render_template('index.html')


# Predict-a-Pitch page
@app.route('/pitch')
def predict_pitch():
    return render_template('pitches.html')


@app.route('/predict', methods=['POST'])
def prediction(pitch_input):
    features = np.array(pitch_input)
    result = model.predict(features)
    return result[0]

def type_encoder(pitch_type):
    vals = []
    for i in range(0, 14):
        vals[i] = 0
    vals[pitch_type] = 1
    return vals


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        pitch_input = request.form.to_dict()
        vals = type_encoder(pitch_input['pitch_type'])
        pitch_input.pop('pitch_type')
        pitch_input = list(pitch_input.values())
        pitch_input.append(vals)
        result = prediction(pitch_input)
        if str(result) == 'S':
        # if int(result) > .5:
            pitch_prediction = 'STEEEEERIKE'
        else:
            pitch_prediction = 'BALL (Or Maybe a hit)!'
        return pitch_prediction


if __name__ == '__Home__':
    app.run(debug=True)
