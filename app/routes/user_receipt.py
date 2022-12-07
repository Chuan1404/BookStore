from app import app
from flask import render_template 
from flask_login import current_user 

from app.controllers import get_all_receipt_by_user_id



def user_receipt():
    data = get_all_receipt_by_user_id(current_user.id)

    return render_template('pages/user_receipt.html')