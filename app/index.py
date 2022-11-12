from app import app
import controllers, models, routes


with app.app_context():
    app.add_url_rule('/', view_func=routes.index)
    app.add_url_rule('/login', view_func=routes.login)
    app.add_url_rule('/register', view_func=routes.register)
    app.add_url_rule('/product', view_func=routes.detail)


if __name__ == '__main__':
    app.run(debug=True)