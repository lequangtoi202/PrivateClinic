from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import cloudinary

app = Flask(__name__)
app.secret_key = '4567890sdfghjklcvbnvb4567fg6yug'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/privateclinic?charset=utf8mb4' % quote(
    'lqt25092002')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app=app)

login = LoginManager(app=app)
login.login_view = 'login_page'
cloudinary.config(cloud_name='dbkikuoyy', api_key='567559374386658', api_secret='rEfNB-gwv6155y2K_G4RGio8rQc')
