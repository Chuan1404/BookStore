from app import app
import controller, modules, routes


with app.app_context():
    app.add_url_rule('/', view_func=routes.index)
    app.add_url_rule('/login', view_func=routes.login)
    app.add_url_rule('/register', view_func=routes.register)


if __name__ == '__main__':
    app.run(debug=True)