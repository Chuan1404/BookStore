from app import app
from flask import render_template
from app.decorators import anonymous_user_checkout
from flask import render_template

@anonymous_user_checkout
def checkout():
    return render_template('pages/login.html')