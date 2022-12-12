from flask import render_template, request
from app.controllers import *
import math

def index():
    from_price = request.args.get('from_price')
    to_price = request.args.get('to_price')
    kw = request.args.get('kw')
    category = request.args.get('category')
    page_number = int(request.args.get('page')) if request.args.get('page') else 1

    # data
    products = get_books(from_price=from_price, to_price=to_price, kw=kw, category=category)
    categories = get_categories()

    # pagnation    
    limit = 6
    pages = math.ceil(len(products) / limit)
    start = (page_number - 1) * limit
    end = (page_number * limit)

    

    if products:
        return render_template('pages/index.html', products=products[start:end], categories=categories, pages=pages)
    return render_template('pages/index.html')




