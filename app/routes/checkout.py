from app import app, db
from flask_login import login_required, current_user
from flask import render_template , session , jsonify ,request
import json
from models import Receipt, Receipt_detail




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
    price=float(data.get('price'))

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



def add_receipt(cart):
    if cart:
        receipt = Receipt(customer_id = current_user)
        db.session.add(receipt)

        for c in cart.values():
            d=Receipt_detail(receipt_id=receipt, book_id=c['id'], amount=c['quantity'],unit_price=c['price'])
            db.session.add(d)
        
        db.session.commit()

@app.route('/api/pay',methods=['post'])
def pay():
    try: 
        add_receipt(session.get('cart'))
        del session['cart']
    except:
        return jsonify({'code':400})
    return jsonify({'code':200})