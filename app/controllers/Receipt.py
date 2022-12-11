from app import db
from app.models import Receipt, Receipt_detail, Order_detail, Order

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


def stats_book_in_receipt(book_id, month=None):
    details = Receipt_detail.query.filter(Receipt_detail.book_id == book_id)
    order_paid = Order.query.filter_by(is_paid=True)

    turnover = 0
    total_amount = 0

    if month:
        pass

    for d in details:
        turnover += d.amount * d.unit_price
        total_amount += d.amount

    for o in order_paid:
        for d in o.detail:
            turnover += d.amount * d.unit_price
            total_amount += d.amount
    return {
        'turnover': turnover,
        'total_amount': total_amount
    }
