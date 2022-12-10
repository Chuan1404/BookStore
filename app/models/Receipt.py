from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey, String
from datetime import datetime
from sqlalchemy.orm import relationship

from app import db


class Receipt(db.Model):
    __tablename__ = 'receipt'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now())
    customer_name = Column(String(100), nullable=False)
    total = Column(Float, nullable=False)

    # FOREIGN KEYS
    saler_id = Column(Integer, ForeignKey('user.id'))

    # RELATIONSHIP
    detail = relationship('Receipt_detail', backref='receipt', lazy=True)

    def __str__(self):
        return f'{self.id}'


class Receipt_detail(db.Model):
    __tablename__ = 'receipt_detail'

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Integer, nullable=False, default=1)
    unit_price = Column(Float, default=0, nullable=0)

    # FOREIGN KEYS
    book_id = Column(Integer, ForeignKey('book.id'), nullable=False)
    receipt_id = Column(Integer, ForeignKey(Receipt.id), nullable=False)
