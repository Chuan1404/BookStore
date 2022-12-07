from app import app
from flask import render_template 
from flask_login import current_user, login_required

from app.controllers import get_all_receipt_by_user_id


@login_required
def user_receipt():
    receipts = get_all_receipt_by_user_id(current_user.id)


    return render_template('pages/user_receipt.html', receipts=receipts)