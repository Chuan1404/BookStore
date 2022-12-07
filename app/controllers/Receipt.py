from app.models import *
from flask import session
from flask_login import current_user
from app import db


def add_receipt(data):

    receipt = Receipt(customer=current_user.id, saler=current_user.id)

    db.session.add(receipt)
    db.session.commit()

    
    if session.get('cart'):
        for c in session.get('cart').values():
            d = Receipt_detail(
                receipt_id=receipt.id, book_id=c['id'], amount=c['quantity'], unit_price=c['price'])
            db.session.add(d)
    
    db.session.commit()

    return {
        'status': 1
    }

def get_all_receipt_by_user_id(user_id):
    # receipt_list = Receipt.query.filter_by(customer_id=user_id).all()
    print(Receipt.query.get(1).__dict__)
    # print(user_id)

