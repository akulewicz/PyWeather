from flask import render_template
from app.weather import get_weather
from app import app


@app.route('/')
def index():
    return render_template('index.html', weather=get_weather())
