from app import app, admin, login_manager
from app.controllers import get_user_by_id
import routes

from flask import request, redirect



with app.app_context():
    app.add_url_rule('/', view_func=routes.index)
    app.add_url_rule('/login', view_func=routes.login, methods=['GET', 'POST'])
    app.add_url_rule('/logout', view_func=routes.logout)
    app.add_url_rule('/register', view_func=routes.register, methods=['GET', 'POST'])
    app.add_url_rule('/product', view_func=routes.detail)
    app.add_url_rule('/checkout', view_func=routes.checkout)
    


@login_manager.user_loader
def load_user(id):
    return get_user_by_id(id)

@login_manager.unauthorized_handler
def unauthorized_handler():
    if request.path.__eq__('/admin/'):
        return redirect('/admin/login')
    return redirect('/login')
    
if __name__ == '__main__':
    app.run(debug=True)