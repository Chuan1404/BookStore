from app import app
from flask import render_template
from flask_login import login_required

# @anonymous_user_checkout
# def checkout():
#     return render_template('pages/login.html')

@login_required
def checkout():
    return render_template('pages/checkout.html')