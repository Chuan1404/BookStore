from app.models import *
from app.controllers import get_book_by_id
from flask import session
from flask_login import current_user
from app import db


def add_order():
    err = ''
    try:
        carts = session.get('cart')
        if carts:
            order = Order(customer_id=current_user.id)

            db.session.add(order)
            db.session.commit()

            for c in carts.values():
                d = Order_detail(
                    order_id=order.id, book_id=c['id'], amount=c['quantity'], unit_price=c['price'])
                db.session.add(d)

            db.session.commit()
        else:
            err = 'Chưa có sản phẩm trong giỏ hàng'
    except Exception as excep:
        err = str(excep)
    
    if err:
        return {
            'status': 0,
            'err': err
        }
    return {
        'status': 1
    }


def get_all_order_by_user_id(user_id):
    order_list = Order.query.filter_by(customer_id=user_id).all()

    for r in order_list:
        for d in r.detail:
            print(d.book)

    return order_list
