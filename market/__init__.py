from flask import Flask,render_template
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/FlaskMarket/new_project/market/market.db'
app.app_context().push()
db = SQLAlchemy(app)


from market import routes


