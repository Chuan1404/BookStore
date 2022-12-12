from flask import render_template, request
from app.controllers import *
def index():
    from_price = request.args.get('from_price')
    to_price = request.args.get('to_price')
    kw = request.args.get('kw')
    category = request.args.get('category')

    products = get_books(from_price=from_price, to_price=to_price, kw=kw, category=category)

    categories = get_categories()
        
    
    if products:
        return render_template('pages/index.html', products=products, categories=categories)
    return render_template('pages/index.html')




