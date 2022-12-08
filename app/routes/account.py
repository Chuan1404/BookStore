from app import app
from flask import render_template 
from flask_login import current_user 



def account():
    print(current_user.address)
    return render_template('pages/account.html')






