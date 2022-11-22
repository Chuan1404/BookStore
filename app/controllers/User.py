from app import db
from flask import render_template

from app.models.User import Customer, User_role, Admin, Warehouse_manager, Staff

def get_user_by_id(id):
    return Customer.query.get(id)

def add_user(username, name, email, phone_number, password):
    err = {}
    # validate form
    exist_user = Customer.query.filter_by(username=username).first()
    print(exist_user)
    if exist_user:
        err['username'] = 'This username has exist on database'
        return {
            'status': 0,
            'err': err
        }
    else: 
        user = Customer(username=username, name=name, email=email, phone_number=phone_number, password=password)
        db.session.add(user)
        db.session.commit()
        return {
            'status': 1
        }

        
