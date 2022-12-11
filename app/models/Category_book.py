from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship, backref
from app import db


class Category(db.Model):
    __tablename__='category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)

    def __str__(self):
            return self.name
    
class Book(db.Model):
    __tablename__='book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False, default=0)
    description = Column(Text)
    author = Column(String(50))
    active = Column(Boolean, default=True)
    amount = Column(Integer, default = 0)
    img = Column(String(100), nullable=False)

    # RELATIONSHIP
    category = relationship('Category', secondary='category_book', lazy='subquery', backref=backref('book', lazy=True))
    note = relationship('Note_detail', backref='book', lazy=True)
    order = relationship('Order_detail', backref='book', lazy=True)
    receipt = relationship('Receipt_detail', backref='book', lazy=True)

    def __str__(self):
        return self.name

db.Table('category_book', 
Column('category_id', Integer, ForeignKey('category.id'), nullable=False, primary_key=True),
Column('book_id',Integer,ForeignKey('book.id'), nullable=False, primary_key=True))
