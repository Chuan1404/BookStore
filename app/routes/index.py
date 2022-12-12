from flask import render_template, request
from app.controllers import *
def index():
    print(request.args)

    products = get_books()
    categories = get_categories()
        
    
    if products:
        return render_template('pages/index.html', products=products, categories=categories)
    return render_template('pages/index.html')




