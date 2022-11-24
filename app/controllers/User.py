from app import db
from app.models import User, User_role
import hashlib

def get_user_by_id(id):
    return User.query.get(id)

def add_user(username, name, email, phone_number, password, user_role):
    errs = {}
    # validate form
    exist_user = User.query.filter_by(username=username).first()
    if exist_user:
        errs['username'] = 'This username has exist on database'
        return {
            'status': 0,
            'errs': errs
        }
    else: 
        hash_password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

        user = User(username=username, name=name, email=email, phone_number=phone_number, password=hash_password, user_role=user_role)
        db.session.add(user)
        db.session.commit()
        return {
            'status': 1
        }

def auth_user(username, password, user_role=User_role.CUSTOMMER):
    hash_password = hashlib.md5(password.strip().encode('utf-8')).hexdigest()

    user = User.query.filter_by(username=username, password=hash_password, user_role=user_role).first()
    
    if(user):
        return {
        'status': 1,
        'user': user
    }
    return {
        'status': 0,
        'err': 'Username or password not correct',
    }
    

        