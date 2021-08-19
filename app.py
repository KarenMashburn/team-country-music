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


# Prediction and encoding functions
@app.route('/predict', methods=['POST'])
def prediction(pitch_input):
    features = np.array(pitch_input).reshape(1, -1)
    result = model.predict(features)
    return result[0]

def type_encoder(p_type):
    vals = []
    for i in range(0, 15):
        vals.append(0)
    vals[int(p_type)] = 1
    return vals


# Predict from model and present result
@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':

        # Collect and clean input data
        pitch_input = request.form.to_dict()
        vals = type_encoder(pitch_input['pitch_type'])
        pitch_input.pop('pitch_type')
        pitch_input = list(pitch_input.values())

        # Append pitch_type values to pitch_input
        for value in vals:  
            pitch_input.append(value)

        # Predict result
        result = prediction(pitch_input)

        # Display result
        if str(result) == 'S':
        # if int(result) > .5:
            pitch_prediction = 'STEEEEERIKE!!'
        else:
            pitch_prediction = 'Not a strike!<br>Get back on that hill and<br>TRY AGAIN'
        return pitch_prediction


if __name__ == '__Home__':
    app.run(debug=True)
