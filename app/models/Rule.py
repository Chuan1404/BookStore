from sqlalchemy import Column, Float, Integer

from app import db


class Rule(db.Model):
    __tablename__='rule'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    receipt_cancel_time = Column(Float, nullable=False, default=48)
    minimum_entry = Column(Integer, nullable=False, default=150)
    minimum_inventory = Column(Integer, nullable=False, default=300)