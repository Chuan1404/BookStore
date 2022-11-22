from app import login_manager
from app.controllers import get_user_by_id, add_user, auth_user
from flask import render_template, request, redirect
from flask_login import login_user

def login():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        result = auth_user(username=username, password=password)

        if result.get('status'):
            login_user(result.get('user'))
            return redirect('/')
        else:
            return render_template('pages/login.html', err=result.get('err'))

    return render_template('pages/login.html')

def register():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        name = request.form.get('name')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        password = request.form.get('password')


        result = add_user(username=username, name=name, email=email, phone_number=phone_number, password=password)
        if result.get('status'):
            return render_template('pages/login.html')
        else:
            return render_template('pages/register.html', err=result.get('err'))
    
    return render_template('pages/register.html')

@login_manager.user_loader
def load_user(id):
    return get_user_by_id(id)