from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class CityForm(FlaskForm):
    city = StringField('Podaj nazwę miejscowości', validators=[DataRequired(), Length(min=2, max=12)])
