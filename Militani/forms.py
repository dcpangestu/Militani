from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired
from Militani.models import Implementasi, Keuntungan, Rancangan

class CriteriaForm(FlaskForm):
	sumberdaya = StringField('Sumberdaya', validators=[DataRequired()])
	investasi = StringField('Investasi', validators=[DataRequired()])
	pengetahuan = PasswordField('Pengetahuan', validators=[DataRequired()])
	keuangan = PasswordField('Keuangan', validators=[DataRequired()])
	submit = SubmitField('Submit')
