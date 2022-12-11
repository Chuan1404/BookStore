from flask import request

from app import app, db
from app.controllers import get_order_by_id

@app.route('/api/pay-order', methods=['post'])
def pay_order():
    id = request.json
    order = get_order_by_id(id)
    if not order:
        return {
            'stautus': 0,
            'err': 'Không có đơn đặt hàng hợp lệ'
        }
    order.is_paid = True

    print('********************', order.__dict__)
    db.session.commit()
    return {
        'status': 1
    }