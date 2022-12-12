from app import db
from app.models import Receipt, Receipt_detail
from flask_login import current_user
from flask import session


def get_receipt_by_id(id):
    return Receipt.query.get(id)


def add_receipt(customer):
    if current_user.is_authenticated:
        receipt = Receipt(saler_id=current_user.id,
                          customer_name=customer['name'], total=customer['total'])
        db.session.add(receipt)
        db.session.commit()
        pay = session.get('pay')

        if not pay:
            pay = {}

        for p in pay.values():
            detail = Receipt_detail(
                receipt_id=receipt.id, book_id=p['id'], amount=p['amount'], unit_price=p['unit_price'])
            db.session.add(detail)

        db.session.commit()

        if session.get('pay'):
            del session['pay']

        return {
            'status': 1,
        }


