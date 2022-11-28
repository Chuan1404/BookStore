from app import app
from flask import render_template
from flask_login import login_required


@login_required
def checkout():
    return render_template('pages/checkout.html')


