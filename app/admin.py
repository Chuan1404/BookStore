from app import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from app.models import User_role

from app.models import Rule, Book, Category, Receipt, Receipt_detail, Received_note, Received_note_detail, User

class AdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role.__eq__(User_role.ADMIN)

class RuleView(AdminView):
    can_export = True
    column_sortable_list = ['minimum_entry', 'minimum_inventory']
    column_labels = {
        'receipt_cancel_time': 'Thời gian huỷ đơn',
        'minimum_entry': 'Số lượng nhập sách tối thiểu',
        'minimum_inventory': 'Số lượng tồn kho tối thiểu'
    }

class UserView(AdminView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    column_sortable_list = ['id', 'name', 'username']
    column_searchable_list = ['name', 'username']
    column_labels = {
        'id': 'ID User',
        'name': 'Họ và tên',
        'username': 'Tên đăng nhập',
        'phone_number': 'Số điện thoại'
    }

class BookView(AdminView):
    # Hiện id sách
    column_display_pk = True

    # Hiện chi tiết sản phẩm
    can_view_details = True

    # Có thể xuất danh sách ra file excel
    can_export = True

    # Hiện thanh search theo tên, mô tả
    column_searchable_list = ['name', 'description']

    # Hiện nút tìm kiếm filter theo tên, giá
    column_filters = ['name', 'price']

    # Thay đổi tên các cột
    column_labels = {
        'id': 'ID',
        'name': 'Tên sách',
        'price': 'Giá sách',
        'description': 'Mô tả',
        'author':'Tác giả'
    }

    # Sắp xếp thứ tự theo id, tên, giá
    column_sortable_list = ['id', 'name', 'price', 'author']

class CategoryView(AdminView):
    column_display_pk = True
    can_view_details = True
    column_searchable_list = ['name', 'description']
    column_filters = ['name', 'description']
    column_sortable_list = ['id', 'name']
    column_labels = {
        'id': 'ID',
        'name': 'Tên thể loại',
        'description': 'Mô tả'
    }

class ReceiptView(AdminView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    column_searchable_list = ['created_at']
    column_sortable_list = ['id']
    column_labels = {
        'id': 'ID',
        'created_at': 'Thời gian lập'
    }

class ReceiptDetailsView(AdminView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    column_sortable_list = ['id', 'amount', 'unit_price']
    column_searchable_list = ['id']
    column_labels = {
        'id': 'ID',
        'amount': 'Số lượng sách',
        'unit_price': 'Tổng tiền'
    }

class ReceiptNoteView(AdminView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    column_searchable_list = ['created_at', 'updated_at']
    column_sortable_list = ['id','created_at','updated_at']
    column_labels = {
        'id': 'ID',
        'created_at': 'Ngày tạo hoá đơn',
        'updated_at': 'Ngày cập nhật'
    }

class ReceiptNoteDetailsView(AdminView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    column_searchable_list = ['id']
    column_sortable_list = ['id', 'amount']
    column_labels = {
        'id': 'ID',
        'amount': 'Tổng số sách'
    }


admin = Admin(app=app, name='Bookstore', template_mode='bootstrap4')

admin.add_view(RuleView(Rule, db.session, name='Rule'))

admin.add_view(UserView(User, db.session, name='User'))

admin.add_view(BookView(Book, db.session, name='Book'))
admin.add_view(CategoryView(Category, db.session, name='Category'))

admin.add_view(ReceiptView(Receipt, db.session, name='Receipt'))
admin.add_view(ReceiptDetailsView(Receipt_detail, db.session, name='Receipt_detail'))

admin.add_view(ReceiptNoteView(Received_note,db.session, name='Received_note'))
admin.add_view(ReceiptNoteDetailsView(Received_note_detail,db.session, name='Received_note_detail'))
