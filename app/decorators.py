from flask_login import current_user
from flask import redirect
from functools import wraps
from flask import render_template
from app.models import User_role

# def anonymous_user_checkout(f):
#     @wraps(f)
#     def decorated_func(*args, **kwargs):
#         if current_user.is_authenticated:
#             return render_template('pages/checkout.html')
#         return f(*args, **kwargs)
#     return decorated_func

def anonymous_user(f): # if user is login, cannot get /login 
    @wraps(f)
    def decorator_func(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect('/')
        return f(*args, **kwargs)
    return  decorator_func

def anonymous_staff(f):
    @wraps(f)
    def decorate_func(*args, **kwargs):
        if current_user.is_authenticated and current_user.user_role != User_role.CUSTOMMER:
            return redirect('/admin/')
        return f(*args, **kwargs)
    return decorate_func

