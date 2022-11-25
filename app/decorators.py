from flask_login import current_user
from flask import redirect
from functools import wraps

from app.models import User_role


def anonymous_user(f):
    @wraps(f)
    def decorated_func(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect('/')
        return f(*args, **kwargs)
    return decorated_func

def anonymous_staff(f):
    @wraps(f)
    def decorate_func(*args, **kwargs):
        if current_user.is_authenticated and current_user.user_role != User_role.CUSTOMMER:
            return redirect('/')
        return f(*args, **kwargs)
    return decorate_func

