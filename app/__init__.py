import sys
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote

# load env file
load_dotenv()

# PYTHONPATH 
sys.path.append('./')

# create app
app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://admin:%s@localhost:3306/quanlysach?charset=utf8mb4' % quote('Admin@123')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app=app)
