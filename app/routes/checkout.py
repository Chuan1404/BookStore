from app import app
from flask import render_template

def checkout():
    return render_template('pages/checkout.html')