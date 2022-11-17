from app import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app.models import Warehouse_manager
from app.models import Rule
from app.models import Book

class RuleView(ModelView):
    pass

class WarehouseView(ModelView):
    pass

class BookView(ModelView):
    # Hiện id sách
    column_display_pk = True

    # Hiện chi tiết sản phẩm
    can_view_detail = True

    # Có thể xuất danh sách ra file excel
    can_export = True

    # Hiện thanh search theo tên, mô tả
    column_searchable_list = ['name', 'description']

    # Hiện nút tìm kiếm filter theo tên, giá
    column_filters = ['name', 'price']

    # Thay đổi tên các cột
    column_lables = {
        'name': 'Tên sách',
        'price': 'Giá sách',
        'description': 'Mô tả',
        'author':'Tác giả'
    }

    # Sắp xếp thứ tự theo id, tên, giá
    column_sortable_list = ['id', 'name', 'price']



admin = Admin(app=app, name='Bookstore', template_mode='bootstrap4')

admin.add_view(ModelView(Rule, db.session, name='Rule'))
admin.add_view(ModelView(Warehouse_manager, db.session, name='Warehouse_manager'))
admin.add_view(BookView(Book, db.session, name='Book'))