from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app import app, db, path

class User(db.Model):
    __abstract__=True
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    phone_number = Column(String(10))

    def login(email, password):
        pass
    def logout():
        pass

class Warehouse_manager(User):
    __tablename__='warehouse_manager'
    __table_args__ = {'extend_existing': True}

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
    __table_args__ = {'extend_existing': True}

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
    __table_args__ = {'extend_existing': True}

    # RELATIONSHIP
    customer_receipt = relationship(f'{path["receipt"]}.Receipt', backref='customer', lazy=True)

    def order_book(): # đặt sách
        pass
    def pay_receipt(): # thanh toán hóa đơn
        pass
