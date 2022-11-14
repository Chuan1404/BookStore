from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app import db, path


class Category(db.Model):
    __tablename__='category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(200))

    # RELATIONSHIP
    category_book = relationship(f'{path["category_book"]}.Category_book', backref='category', lazy=True)

    
class Book(db.Model):
    __tablename__='book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False, default=0)
    description = Column(String(200))
    author = Column(String(50))

    # RELATIONSHIP
    book_received_note = relationship(f'{path["received_note"]}.Received_note_detail', backref='book', lazy=True)
    book_category = relationship(f'{path["category_book"]}.Category_book', backref='book', lazy=True)
    book_receipt = relationship(f'{path["receipt"]}.Receipt_detail', backref='book', lazy=True)

class Category_book(db.Model):
    __tablename__='category_book'

    id = Column(Integer, primary_key=True, autoincrement=True)

    # FOREIGN KEYS
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    book_id = Column(Integer, ForeignKey(Book.id), nullable=False)
