import requests
from flask import Flask, request, jsonify
from joblib import dump, load
import json
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

app = Flask(__name__)

@app.route('/predict/', methods=['GET'])
def predict():
    """Predict several elements"""
    input_data_shifted = pd.DataFrame({f't{k}': input_data.shift(k) for k in range(30)})
    input_data_shifted = input_data_shifted[~input_data_shifted.isna().any(axis=1)].drop(columns='t0')
    prediction = np.round(clf_load.predict(input_data_shifted), decimals=0)
    return str(prediction)

if __name__ == '__main__':
    clf_load = load('model.joblib')
    input_data = load('input_data_2020.csv')
    app.run()
