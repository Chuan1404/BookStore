from app.models import *
from app.controllers import get_book_by_id 
from flask import session
from flask_login import current_user
from app import db


def add_receipt(data):

    receipt = Receipt(customer_id=current_user.id, saler_id=current_user.id)

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
    receipt_list = Receipt.query.filter_by(customer_id=user_id).all()
    return receipt_list


def get_detail_receipt(receipt_id):
    details_list = Receipt_detail.query.filter_by(receipt_id=receipt_id).all()
    res = []
    for d in details_list:
        res.append({
            'id': d.id,
            'book': get_book_by_id(d.book_id),
            'amount': d.amount,
            'unit_price': d.unit_price,
            'total': d.amount * d.unit_price
        })

    if res:
        return {
            'status': 1,
            'data': res
        }
    else:
        return {
            'status': 0,
            'data': 'Receipt error'
        }