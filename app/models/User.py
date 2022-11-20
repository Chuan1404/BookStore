from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app import app, db, path
from enum import Enum as UserEnum

class User_role(UserEnum):
    ADMIN = 0
    CUSTOMMER = 1
    WAREHOUSE_MANAGER = 2
    STAFF = 3

class User(db.Model):
    __abstract__=True
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    phone_number = Column(String(10))

class Warehouse_manager(User):
    __tablename__='warehouse_manager'


    def book_entry(book_id, amount): # nhập sách
        pass
class Admin(User):
    __tablename__='admin'
    __table_args__ = {'extend_existing': True}

    # RELATIONSHIP
    received_note = relationship(f'{path["received_note"]}.Received_note', backref='admin', lazy=True)

    def statistical(view): # thống kê sách
        pass
    def delete_book(id): # xóa sách
        pass
    def update_book(id): # cập nhật sách
        pass
    def add_book(id): # thêm sách
        pass
    def find_book(id): # tìm sách
        pass
    def create_received_note(): # tạo phiếu nhập hàng
        pass
    def change_rule(): # thay đổi quy định
        pass

    

class Staff(User):
    __tablename__='staff'

    # RELATIONSHIP
    staff_receipt = relationship(f'{path["receipt"]}.Receipt', backref='staff', lazy=True)

    def input_code(): # nhập mã
        pass
    def create_receipt(): # tạo hóa đơn
        pass
    def payment_confirm(id): # xác nhận thanh toán hóa đơn
        pass

class Customer(User):
    __tablename__='customer'

    # RELATIONSHIP
    customer_receipt = relationship(f'{path["receipt"]}.Receipt', backref='customer', lazy=True)

    def order_book(): # đặt sách
        pass
    def pay_receipt(): # thanh toán hóa đơn
        pass

