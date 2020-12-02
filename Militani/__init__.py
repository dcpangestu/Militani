from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
import pickle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd2a0e39be0acfb1a5e1781d37917dd18'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://jeernqqq:KhSoo90yLnTSeQfJMIqXUnT3C1ViegqP@suleiman.db.elephantsql.com:5432/jeernqqq'
db = SQLAlchemy(app)

from Militani import routes
