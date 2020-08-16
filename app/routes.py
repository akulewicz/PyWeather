from flask import render_template
from app.forms import CityForm
from app.weather import get_weather
from app import app


@app.route('/', methods=['GET', 'POST'])
def index():
    city = None
    form = CityForm()
    if form.validate_on_submit():
        city = form.city.data
        form.city.data = ''
    return render_template('index.html', weather=get_weather(city=city), form=form, city=city)
