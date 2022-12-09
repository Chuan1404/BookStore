from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey, Boolean
from datetime import datetime
from sqlalchemy.orm import relationship

from app import db

class Order(db.Model):
    __tablename__='order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    is_paid = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now())


    # FOREIGN KEYS
    customer_id = Column(Integer, ForeignKey('user.id'))
 
    # RELATIONSHIP
    detail = relationship('Order_detail', backref='order', lazy=True)

    def __str__(self):
        return f'{self.id}'



class Order_detail(db.Model):
    __tablename__='order_detail'

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Integer, nullable=False, default=1)
    unit_price = Column(Float, default=0, nullable=0) 

    # FOREIGN KEYS
    book_id = Column(Integer, ForeignKey('book.id'), nullable=False)
    order_id = Column(Integer, ForeignKey(Order.id), nullable=False)

    
    