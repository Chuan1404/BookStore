from app import app
from flask import render_template

def login():
    return render_template('pages/login.html')

def register():
    return render_template('pages/register.html')
