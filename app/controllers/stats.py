from app import db
from app.models import *
from app.controllers import get_categories, stats_book_in_receipt
from sqlalchemy import func


def category_turnover(month=None):
    categories = get_categories()
    render_categories = {}
    total_book = 0

    for c in categories:
        render_categories[c.id] = {
            'name': c.name,
            'turnover': 0,
            'total_amount': 0,
            'rate': 0
        }
        for b in c.book:
            res = stats_book_in_receipt(book_id=b.id)
            render_categories[c.id]['turnover'] += res['turnover']
            render_categories[c.id]['total_amount'] += res['total_amount']
            total_book += res['total_amount']
    
    for r in render_categories.values():
            r['rate'] = round(r['total_amount'] / (total_book * 0.01), 2) if r['total_amount'] else 0
    return render_categories
