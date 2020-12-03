from flask import render_template, url_for, flash, redirect, request, json
from Militani import app, db
from Militani.forms import CriteriaForm
from Militani.models import Implementasi, Keuntungan, Rancangan
from flask_session import Session
import numpy as np
import urllib.request
import pickle

def oneHot(var):
    enc = []
    feat_col = ['Memungkinkan', 'Mudah', 'Sangat Sulit', 'Impas', 'Kerugian Tinggi', 'Rugi', 'Untung Sedang', 'Untung Tinggi']
    for feat in feat_col:
        if feat in var:
            enc.append(1)
        else:
            enc.append(0)

    enc = np.asarray(enc)
    enc = enc.reshape(1, -1)
    return enc


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def results():
    form = request.form
    if request.method == 'POST':
        with open("Militani/models/model_miltani.sav","rb") as f:
            model = pickle.load(f)
        var = oneHot(form)
        plant = model.predict(var)
        return render_template('recomend.html', plant=plant)

@app.route('/rancangan')
def rancangan():
	form = CriteriaForm()
	implementasi = Implementasi.query.filter_by(sumberdaya=form.sumberdaya.data, investasi=form.investasi.data).first()
	keuntungan = Keuntungan.query.filter_by(pengetahuan=form.pengetahuan.data, keuangan=form.keuangan.data).first()
	rancangan = Rancangan.query.filter_by(pengetahuan=keuntungan.keuntungan, keuangan=form.keuangan.keuangan).first()
	return render_template('rancangan.html', imp=implementasi, ktg=keuntungan, rcg=rancangan, title=rancangan)