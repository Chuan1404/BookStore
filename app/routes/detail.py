from app.controllers import get_book_by_id
from flask import render_template

def detail(id):
    product = get_book_by_id(id)
    return render_template('pages/detail.html', product=product) 

   


