from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '6734653887sdfbd7f98439dsf4'

from app import routes