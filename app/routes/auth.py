from app.controllers import add_user, auth_user
from app.models import User_role
from app.decorators import anonymous_user
from flask import render_template, request, redirect, session
from flask_login import login_user, logout_user


@anonymous_user
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


        result = add_user(username=username, name=name, email=email, phone_number=phone_number, password=password, user_role=User_role.CUSTOMMER)
        if result.get('status'):
            user = auth_user(username=username, password=password).get('user')
            login_user(user)
            return redirect('/')
        else:
            return render_template('pages/register.html', errs=result.get('errs'))
    
    return render_template('pages/register.html')

def logout():
    logout_user()
    if session and session['cart']:
        del session['cart']
    return redirect('/login')

