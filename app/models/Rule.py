from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

from app import app, db

class Rule(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    receipt_cancel_time = Column(Float, nullable=False, default=48)
    minimum_entry = Column(Integer, nullable=False, default=150)
    minimum_inventory = Column(Integer, nullable=False, default=300)