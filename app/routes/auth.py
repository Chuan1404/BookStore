from app import login_manager
from app.controllers import get_user_by_id, add_user
from app.models.User import User_role 
from flask import render_template, request, redirect

def login():
    
    return render_template('pages/login.html')

def register():
    if request.method.__eq__('POST'):
        err = {}

        username = request.form.get('username')
        name = request.form.get('name')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        password = request.form.get('password')

        add_user(username=username, name=name, email=email, phone_number=phone_number, password=password, role=User_role.CUSTOMMER)

        if err:
            return render_template('pages/register.html', err=err)
        else:
            return redirect('/login')
    return render_template('pages/register.html')

@login_manager.user_loader
def load_user(id):
    return get_user_by_id(id)