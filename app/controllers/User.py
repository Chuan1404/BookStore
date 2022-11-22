from app import db
from app.models.User import Customer
import hashlib
from flask_login import login_user

def get_user_by_id(id):
    return Customer.query.get(id)

def add_user(username, name, email, phone_number, password):
    errs = {}
    # validate form
    exist_user = Customer.query.filter_by(username=username).first()
    if exist_user:
        errs['username'] = 'This username has exist on database'
        return {
            'status': 0,
            'errs': errs
        }
    else: 
        hash_password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

        user = Customer(username=username, name=name, email=email, phone_number=phone_number, password=hash_password)
        db.session.add(user)
        db.session.commit()
        return {
            'status': 1
        }

def auth_user(username, password):
    hash_password = hashlib.md5(password.strip().encode('utf-8')).hexdigest()

    user = Customer.query.filter_by(username=username, password=hash_password).first()

    if(user):
        return {
        'status': 1,
        'user': user
    }
    return {
        'status': 0,
        'err': 'Username or password not correct'
    }
    

        