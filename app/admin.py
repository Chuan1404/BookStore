from app import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app.models.User import Warehouse_manager
from app.models.Rule import Rule

admin = Admin(app=app, name='Bookstore', template_mode='bootstrap4')
admin.add_view(ModelView(Rule, db.session, name='Rule'))
admin.add_view(ModelView(Warehouse_manager, db.session, name='Warehouse_manager'))