from flask import request, redirect, flash, session
from flask_admin import AdminIndexView, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import login_user, current_user, login_required, logout_user

from app.decorators import anonymous_staff
from app.models import *
from app.controllers import *

from app import db

from wtforms import TextAreaField
from wtforms.widgets import TextArea

# Admin Model View


class AdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == User_role.ADMIN

# Admin, Warehouse, Saler BaseView


class AuthenticatedView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class AdminBaseView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == User_role.ADMIN


class WarehouseView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == User_role.WAREHOUSE_MANAGER


class SalerView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == User_role.SALER


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()

# Index Admin View


class IndexView(AdminIndexView):
    @expose('/')
    @login_required
    def index(self):
        return self.render('admin/index.html')

    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role != User_role.CUSTOMMER

    def inaccessible_callback(self, name, **kwargs):
        return redirect('/admin/login')

# Login View


class LoginView(BaseView):
    @expose('/', methods=('GET', 'POST'))
    @anonymous_staff
    def index(self):
        if request.method.__eq__('POST'):
            username = request.form.get('username')
            password = request.form.get('password')
            user_role = request.form.get('role')

            if user_role == '0':
                user_role = User_role.ADMIN
            elif user_role == '2':
                user_role = User_role.WAREHOUSE_MANAGER
            elif user_role == '3':
                user_role = User_role.SALER

            result = auth_user(username=username,
                               password=password, user_role=user_role)

            if result.get('status'):
                login_user(result.get('user'))
                return redirect('/admin/')
            else:
                return self.render('admin/login.html', err=result.get('err'))
        return self.render('admin/login.html')

# Logout View


class LogoutView(AuthenticatedView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')

# Warehouse View


class ImportBookView(WarehouseView):
    @expose('/', methods=('GET', 'POST'))
    def index(self):
        # 2022-11-29 19:57:12
        current_date = request.args.get('current_date')
        if current_date:
            date_split = current_date.split('-')
            res = data_import_page(date=datetime(
                int(date_split[0]), int(date_split[1]), int(date_split[2])))
        else:
            res = data_import_page()

        if res:
            return self.render('admin/import_book.html', note_detail=res)
        return self.render('admin/import_book.html')

# Sale View


class SaleView(SalerView):
    @expose('/', methods=('GET', 'POST'))
    def index(self):
        if request.method == 'POST':
            print(request.form)
            res = add_receipt(request.form)
            return redirect('/admin/sale/')
        else:
            pay_session = session.get('pay')
            return self.render('admin/sale.html', books=pay_session)

# Pay receipt View


class PayReceiptView(SalerView):
    @expose('/', methods=('GET', 'POST'))
    def index(self):
        if request.method == "POST":
            id = request.form['order_id']
            res = get_data_render_pay_order_page(id)

            if res['status']:
                return self.render('admin/pay_order.html', order=res['data'])
            else:
                return self.render('admin/pay_order.html', err=res['err'])
        return self.render('admin/pay_order.html')

# Admin View


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

    # def on_model_change(self, form, model, is_created):
    #     if is_created:
    #         pass


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
        'author': 'Tác giả'
    }

    # Sắp xếp thứ tự theo id, tên, giá
    column_sortable_list = ['id', 'name', 'price', 'author']

    extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']
    form_overrides = {
        'description': CKTextAreaField
    }


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
    extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']
    form_overrides = {
        'description': CKTextAreaField
    }


class OrderView(AdminView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    column_searchable_list = ['created_at']
    column_sortable_list = ['id']
    column_labels = {
        'id': 'ID',
        'created_at': 'Thời gian lập'
    }


class OrderDetailsView(AdminView):
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


class NoteView(AdminView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    column_searchable_list = ['created_at', ]
    column_sortable_list = ['id', 'created_at']
    column_labels = {
        'id': 'ID',
        'import_at': 'Ngày nhập',
        'created_at': 'Ngày tạo hoá đơn',
    }


class NoteDetailsView(AdminView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    can_edit=False
    column_searchable_list = ['id']
    column_sortable_list = ['id', 'amount']
    column_labels = {
        'id': 'ID',
        'amount': 'Tổng số sách'
    }

    def on_model_change(self, form, model, is_created):
        if is_created:
            err = ''
            book = get_book_by_id(model.book.id)

            # check amount of model
            if book and book.amount >= 300:
                err = 'Số lượng sản phẩm đã trên 300'
            else:
                if model.amount < 150:
                    err = 'Số lượng nhập phải trên 150'

            # check model exist on database or not
            data_exist = Note_detail.query.filter(
                Note_detail.book_id == model.book_id, Note_detail.note_id == model.note_id).all()
            print(model.book_id,  model.note_id)
            print(data_exist)
            if len(data_exist) >= 1:
                err = 'Sản phẩm đã tồn tại'

            if err:
                flash(err, 'error')
                self.delete_model(model)
            else:
                flash('Create success', 'success')


class AddressView(AdminView):
    column_display_pk = True
    can_view_details = True

# Stats View


class StatsView(AdminBaseView):
    @expose('/')
    def index(self):
        month = request.args.get('month') if request.args.get('month') else datetime.now().month
        year = request.args.get('year') if request.args.get('year') else datetime.now().year


        categories = category_turnover(month, year)
        books = book_stats(month, year)
        return self.render('admin/stats.html', categories=categories, books=books)
