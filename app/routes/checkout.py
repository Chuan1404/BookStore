from app import app, db
from flask_login import login_required
from flask import render_template, session, jsonify, request, redirect, flash
from app.controllers import add_order, add_address


@login_required
def checkout():
    return render_template('pages/checkout.html')

# Gio hang


@app.route('/api/add-cart', methods=['post'])
def add_to_cart():
    data = request.json
    id = str(data.get('id'))
    img = data.get('img')
    name = data.get('name')
    price = float(data.get('price'))
    amount = int(data.get('amount'))

    cart = session.get('cart')
    if not cart:
        cart = {}

    if id in cart:
        cart[id]['quantity'] = amount
    else:
        cart[id] = {
            'id': id,
            'img': img,
            'name': name,
            'price': price,
            'quantity': amount
        }
    session['cart'] = cart

    return jsonify(count_cart(cart))


@app.route('/api/checkout', methods=['post'])
def checkout_api():
    data = request.json
    order_res = add_order()

    if order_res['status']:
        add_address(city_id=int(data['city']), district_id=int(
            data['district']), ward_id=int(data['ward']), address=data['address'])
        del session['cart']
        return jsonify({'status': 200})
    else:
        return jsonify({
            'status': 400,
            'err': order_res['err']
        })


@app.route('/api/checkout/delete', methods=['post'])
def delete_to_cart():
    id = request.json

    cart = session.get('cart')

    del cart[id]

    session['cart'] = cart

    return jsonify({'status': 200})


def count_cart(cart):
    total_quantity, total_amount, total_header_cart = 0, 0, 0

    if cart:
        for c in cart.values():
            if c['id'] not in cart.values():
                total_header_cart += 1
            total_quantity += c['quantity']
            total_amount += c['quantity'] * c['price']

    return {
        'total_quantity': total_quantity,
        'total_amount': total_amount,
        'total_header_cart': total_header_cart
    }
