from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'a8fa3ccca78870f0cd24ec2b'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from market import routes