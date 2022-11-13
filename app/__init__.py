import sys
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote

# variable
path = {
    'category_book': 'app.models.Category_book',
    'receipt': 'app.models.Receipt',
    'received_note': 'app.models.Received_note',
    'rule': 'app.models.Rule',
    'user': 'app.models.User',
}

# load env file
load_dotenv()

# PYTHONPATH 
sys.path.append('./')

# create app
app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://admin:%s@localhost:3306/quanlysach?charset=utf8mb4' % quote('Admin@123')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db=SQLAlchemy(app=app)
