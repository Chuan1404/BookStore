from app import login_manager
from app.controllers import get_user_by_id
from flask import render_template, request

def login():
    
    return render_template('pages/login.html')

def register():
    if request.method.__eq__('POST'):
        return request.form
    return render_template('pages/register.html')

@login_manager.user_loader
def load_user(id):
    return get_user_by_id(id)