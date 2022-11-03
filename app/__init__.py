import sys
from flask import Flask
from dotenv import load_dotenv

# load env file
load_dotenv()

# PYTHONPATH 
sys.path.append('./')

# create app
app = Flask(__name__)
