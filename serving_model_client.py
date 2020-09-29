import requests
from flask import Flask, request
from joblib import dump, load
import pickle
import json
import pandas as pd

if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/predict_year/'
    y_pred = load('pred_2020_LES 4 MONTAGNES.pkl')
    y_pred_dict = pd.DataFrame(y_pred).T.to_dict()
    data_json = json.dumps(y_pred_dict)
    print(data_json)
    r = requests.post(url, json=data_json)
    pred_text = r.text[1:-1].replace('\'', '').split(' ')
    print('Predictions:\n')
    # for index, element in enumerate(pred_text):
    #     print('Prediction of sample ' + str(index) + ': ' + element)

# X_test_dict = X_test.T.to_dict()
#     data_json = json.dumps(X_test_dict)
#     r = requests.post(url, json=data_json)
#     pred_text = r.text[1:-1].replace('\'', '').split(' ')