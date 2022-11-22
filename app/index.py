from app import app
import routes



with app.app_context():
    app.add_url_rule('/', view_func=routes.index)
    app.add_url_rule('/login', view_func=routes.login, methods=['GET', 'POST'])
    app.add_url_rule('/logout', view_func=routes.logout)
    app.add_url_rule('/register', view_func=routes.register, methods=['GET', 'POST'])
    app.add_url_rule('/product', view_func=routes.detail)
    app.add_url_rule('/checkout', view_func=routes.checkout)
    




if __name__ == '__main__':
    app.run(debug=True)