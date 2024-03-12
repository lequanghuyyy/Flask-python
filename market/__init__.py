from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY']='lequanghuywebflask'
db = SQLAlchemy(app)

from market import routes
with app.app_context():
 db.create_all()
