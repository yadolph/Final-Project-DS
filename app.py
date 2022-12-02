from flask import Flask, render_template, request
import numpy as np
import pickle


app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def submit_form():
    return render_template('submit.html')


@app.route('/calculate/', methods=('GET', 'POST'))
def calculate_params():

    with open('model_w.pkl', 'rb') as f:
        model_w = pickle.load(f)
    with open('model_d.pkl', 'rb') as f:
        model_d = pickle.load(f)

    iw_inp = request.form['IW']
    if_inp = request.form['IF']
    vw_inp = request.form['VW']
    fp_inp = request.form['FP']

    user_input = [int(iw_inp), int(if_inp), float(vw_inp), int(fp_inp)]

    w_result = round(float(model_w.predict(np.array(user_input).reshape(1, -1))), 2)
    d_result = round(float(model_d.predict(np.array(user_input).reshape(1, -1))), 2)

    return render_template('result.html', w_result=w_result, d_result=d_result)