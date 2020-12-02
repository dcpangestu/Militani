from flask import render_template, url_for, flash, redirect, request, json
from Militani import app, db
from Militani.forms import CriteriaForm
from Militani.models import Implementasi, Keuntungan, Rancangan
from flask_session import Session
import urllib.request
import pickle

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def results():
    form = request.form
    if request.method == 'POST':
        model = pickle.load("/models/model_militani.sav")
        var = form['year']
        plant = model.predict(var)
        return render_template('result.html', plant=plant)

@app.route('/rancangan')
def rancangan():
	form = CriteriaForm()
	implementasi = Implementasi.query.filter_by(sumberdaya=form.sumberdaya.data, investasi=form.investasi.data).first()
	keuntungan = Keuntungan.query.filter_by(pengetahuan=form.pengetahuan.data, keuangan=form.keuangan.data).first()
	rancangan = Rancangan.query.filter_by(pengetahuan=keuntungan.keuntungan, keuangan=form.keuangan.keuangan).first()
	return render_template('rancangan.html', imp=implementasi, ktg=keuntungan, rcg=rancangan, title=rancangan)