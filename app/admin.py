from app import app, db
from app.models import *
from app.routes import *

from flask_admin import Admin




    
admin = Admin(app=app, name='Bookstore', template_mode='bootstrap4', index_view=IndexView())

admin.add_view(LoginView(endpoint='/login'))

admin.add_view(RuleView(Rule, db.session, name='Rule'))

admin.add_view(UserView(User, db.session, name='User'))

admin.add_view(BookView(Book, db.session, name='Book'))
admin.add_view(CategoryView(Category, db.session, name='Category'))

admin.add_view(ReceiptView(Receipt, db.session, name='Receipt'))
admin.add_view(ReceiptDetailsView(Receipt_detail, db.session, name='Receipt_detail'))

admin.add_view(ReceiptNoteView(Received_note,db.session, name='Received_note'))
admin.add_view(ReceiptNoteDetailsView(Received_note_detail,db.session, name='Received_note_detail'))
