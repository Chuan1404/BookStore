from app import app, db
from . import Category_book, Receipt, Received_note

from app.models.User import Warehouse_manager

from app.models.Rule import Rule 

from app.models.Category_book import Book



with app.app_context():
    db.create_all()