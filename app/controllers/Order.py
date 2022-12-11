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

    return order_list


def get_order_by_id(id):
    return Order.query.get(id)


def get_data_render_pay_order_page(id):
    order = get_order_by_id(id)
    if not order:
        return {
            'status': 0,
            'err': 'Không thấy đơn hàng phù hợp'
        }
    else:
        data = {
            'id': order.id,
            'is_paid': order.is_paid,
            'list': [],
            'total': 0
        }
        for d in order.detail:
            book = get_book_by_id(d.book_id)
            data['total'] += d.amount * d.unit_price
            data['list'].append({
                'book': book,
                'amount': d.amount,
                'unit_price': d.unit_price
            })
        return {
            'status': 1,
            'data': data,
        }
