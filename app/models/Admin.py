from flask import request, redirect
from flask_admin import AdminIndexView, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import login_user, current_user, login_required

from app.decorators import anonymous_staff


from app.models import User_role
from app.controllers import auth_user

    
class AdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == User_role.ADMIN

class WarehouseView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == User_role.WAREHOUSE_MANAGER


class SalerView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == User_role.SALER

class IndexView(AdminIndexView):
    @expose('/')    
    @login_required
    def index(self):
        return self.render('admin/index.html')
    def is_accessible(self):
            return current_user.is_authenticated and current_user.user_role != User_role.CUSTOMMER
    def inaccessible_callback(self, name, **kwargs):
        return redirect('/admin/login')

class LoginView(BaseView):
    @expose('/', methods=('GET', 'POST'))
    @anonymous_staff
    def index(self):
        if request.method.__eq__('POST'):
            username = request.form.get('username')
            password = request.form.get('password')
            user_role = request.form.get('role')

            if user_role == '0': user_role = User_role.ADMIN
            elif user_role == '2': user_role = User_role.WAREHOUSE_MANAGER
            elif user_role == '3': user_role = User_role.SALER

            result = auth_user(username=username, password=password,user_role=user_role)

            if result.get('status'):
                login_user(result.get('user'))
                return redirect('/admin/')
            else:
                return self.render('admin/login.html', err = result.get('err'))
        return self.render('admin/login.html')



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
