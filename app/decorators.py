from app import app
from flask_login import current_user
from flask import redirect ,render_template , session , jsonify ,request
from functools import wraps
from app.models import User_role

# def anonymous_user_checkout(f):
#     @wraps(f)
#     def decorated_func(*args, **kwargs):
#         if current_user.is_authenticated:
#             return render_template('pages/checkout.html')
#         return f(*args, **kwargs)
#     return decorated_func

def anonymous_user(f): # if user is login, cannot get /login 
    @wraps(f)
    def decorator_func(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect('/')
        return f(*args, **kwargs)
    return  decorator_func

def anonymous_staff(f):
    @wraps(f)
    def decorate_func(*args, **kwargs):
        if current_user.is_authenticated and current_user.user_role != User_role.CUSTOMMER:
            return redirect('/admin/')
        return f(*args, **kwargs)
    return decorate_func


# Gio hang
@app.route('/api/add-cart',methods=['post'])
def add_to_cart():
    data=request.json
    id = str(data.get('id'))
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

