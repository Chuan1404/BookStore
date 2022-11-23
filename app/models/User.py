from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app import db
from enum import Enum as UserEnum
from flask_login import UserMixin

class User_role(UserEnum):
    ADMIN = 0
    CUSTOMMER = 1
    WAREHOUSE_MANAGER = 2
    STAFF = 3

class User(db.Model, UserMixin):
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    phone_number = Column(String(10))
    user_role = Column(Enum(User_role), nullable=False)

    # RELATION SHIP
    customer_receipt = relationship('Receipt', backref='customer_receipt', lazy=True)
    staff_receipt = relationship('Receipt', backref='staff_receipt', lazy=True)

    admin_received_note = relationship('Received_note', backref='admin_received_note', lazy=True)

    

