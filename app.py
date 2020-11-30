from flask import Flask, render_template, request, redirect, jsonify
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def results():
    form = request.form
    if request.method == 'POST':
        model = pickle.load("/models/blablabla.bla")
        var = form['year']
        plant = model.predict(var)
        return render_template('result.html', plant=plant)