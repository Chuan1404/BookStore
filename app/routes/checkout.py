from app import app
from flask_login import login_required
from flask import render_template , session , jsonify ,request
import json



@login_required
def checkout():
    return render_template('pages/checkout.html')

# PS: T không dẫn đường dẫn ngược ra ngoài được :)))))
# Gio hang
@app.route('/api/add-cart',methods=['post'])
def add_to_cart():
    data=request.json
    id = str(data.get('id'))
    img = data.get('img')
    name=data.get('name')
    price=data.get('price')


    cart=session.get('cart')
    if not cart:
        cart={}

    if id in cart:
        cart[id]['quantity'] = cart[id]['quantity']+1
    else:
        cart[id]={
            'id':id,
            'img': img,
            'name':name,
            'price':price,
            'quantity':1
        }
    session['cart']=cart

    return jsonify(count_cart(cart))




def count_cart(cart):
    total_quantity,total_amount =0,0
    if cart:
        for c in cart.values():
            total_quantity +=c['quantity']
            total_amount +=c['quantity'] * c['price']

    return{
        'total_quantity':total_quantity,
        'total_amount':total_amount
    }




