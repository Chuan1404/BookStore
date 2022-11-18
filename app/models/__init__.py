from app import app, db
from . import Category_book, Receipt, Received_note

from app.models.User import Warehouse_manager, Staff, Customer

from app.models.Rule import Rule 

from app.models.Category_book import Book, Category

from app.models.Receipt import Receipt, Receipt_detail

from app.models.Received_note import Received_note, Received_note_detail


with app.app_context():
    db.create_all()