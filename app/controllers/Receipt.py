from app.models import *
from app.controllers import get_book_by_id 
from flask import session
from flask_login import current_user
from app import db


def add_receipt(data):
    try:
        receipt = Receipt(customer_id=current_user.id, saler_id=current_user.id)

        db.session.add(receipt)
        db.session.commit()

        if session.get('cart'):
            for c in session.get('cart').values():
                d = Receipt_detail(
                    receipt_id=receipt.id, book_id=c['id'], amount=c['quantity'], unit_price=c['price'])
                db.session.add(d)

        db.session.commit()
    except Exception as err:
        return {
            'status': 0,
            'err': str(err)
        }
    return {
        'status': 1
    }


def get_all_receipt_by_user_id(user_id):
    receipt_list = Receipt.query.filter_by(customer_id=user_id).all()

    for r in receipt_list:
        for d in r.detail:
            print(d.book)
        

    return receipt_list