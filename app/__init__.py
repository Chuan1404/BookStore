import sys
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_login import LoginManager



# load env file
load_dotenv()

# PYTHONPATH 
sys.path.append('./')

# create app
app = Flask(__name__)

#Admin su dung bien de save san pham
app.secret_key = '*&^%(&^%##&())&&^%$&%$^^'

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://admin:%s@localhost:3306/quanlysach?charset=utf8mb4' % quote('Admin@123')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# setup database
db=SQLAlchemy(app=app)

# setup login
login_manager = LoginManager(app=app)