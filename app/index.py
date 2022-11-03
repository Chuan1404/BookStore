from app import app
import controller, modules, routes

with app.app_context():
    app.add_url_rule('/', view_func=routes.index)

if __name__ == '__main__':
    app.run(debug=True)
