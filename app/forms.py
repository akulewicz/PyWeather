from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class CityForm(FlaskForm):
    city = StringField('Miasto dla którego chcesz sprawdzić pogodę', validators=[DataRequired(), Length(min=2, max=12)])
