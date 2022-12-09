from app import app
from flask import session, request, jsonify
from app.controllers import get_book_by_id


@app.route('/api/pay/add', methods=['POST'])
def add_to_sale():

    id = request.json

    book = get_book_by_id(id)

    if not book:
        return jsonify({'status': 400, 'err': 'Sản phẩm không tồn tại'})

    pay = session.get('pay')

    if not pay:
        pay = {}

    if id in pay:
        pay[id]['amount'] = pay[id]['amount'] + 1
    else:
        pay[id] = {
            'id': book.id,
            'name': book.name,
            'img': book.img,
            'author': book.author,
            'amount': 1,
            'unit_price': book.price
        }

    session['pay'] = pay

    return jsonify({'status': 200})


@app.route('/api/pay/delete', methods=['POST'])
def delete_to_sale():
    id = request.json

    pay = session.get('pay')

    del pay[id]

    session['pay'] = pay

    return jsonify({'status': 200})


