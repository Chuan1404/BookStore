from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app import app, db

class User(db.Model):
    __abstract__=True
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    def login(email, password):
        pass
    def logout():
        pass

class WarehouseManager(User):
    __tablename__='warehouse_manager'

    def nhapSach(book_id, amount):
        pass
class Admin(User):
    __tablename__='admin'

    # RELATIONSHIP
    phieu_nhap_sach = relationship('PhieuNhapSach', backref='admin', lazy=True)

class Staff(User):
    __tablename__='staff'

class Customer(User):
    __tablename__='customer'
