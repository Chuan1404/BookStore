from app import app, db
from app.models import *

from flask_admin import Admin




    
admin = Admin(app=app, name='Bookstore', template_mode='bootstrap4', index_view=IndexView())


admin.add_view(LoginView(endpoint='/login', name=''))
admin.add_view(ImportBookView(name='Nhập sách', endpoint='/import'))
admin.add_view(SaleView(name='Bán hàng', endpoint='/sale'))

admin.add_view(RuleView(Rule, db.session, name='Rule'))

admin.add_view(UserView(User, db.session, name='User'))

admin.add_view(BookView(Book, db.session, name='Book'))
admin.add_view(CategoryView(Category, db.session, name='Category'))

admin.add_view(OrderView(Order, db.session, name='Đơn hàng'))
admin.add_view(OrderDetailsView(Order_detail, db.session, name='CT Đơn hàng'))

admin.add_view(ReceiptView(Receipt, db.session, name='Hóa đơn'))
admin.add_view(ReceiptDetailsView(Receipt_detail, db.session, name='CT Hóa đơn'))

admin.add_view(NoteView(Note,db.session, name='Phiếu nhập'))
admin.add_view(NoteDetailsView(Note_detail,db.session, name='CT Phiếu nhập'))

admin.add_view(AddressView(Address, db.session, name='Địa chỉ'))

admin.add_view(LogoutView(name='Log out'))
