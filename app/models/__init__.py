from app import app, db
from . import User, Category_book, Receipt, Received_note, Rule



with app.app_context():
    db.create_all()