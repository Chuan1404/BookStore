from flask import render_template
from app.controllers import *
def index():
    products = get_books()
    categories = get_categories()
    if products:
        return render_template('pages/index.html', products=products, categories=categories)
    return render_template('pages/index.html')




