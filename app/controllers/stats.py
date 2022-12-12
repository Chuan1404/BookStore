from app import db
from app.models import Receipt_detail, Order, Order_detail, Receipt
from app.controllers import get_categories, get_books, convert_categories_to_str
from datetime import datetime 

def stats_category_in_receipt(book_id, month):
    # receipt = Receipt.query.filter(Receipt.created_at.month == month)

    # print(receipt)

    details = Receipt_detail.query.filter(Receipt_detail.book_id == book_id)
    order_paid = Order.query.filter_by(is_paid=True)

    turnover = 0
    total_amount = 0

    if month:
        pass

    for d in details:
        turnover += d.amount * d.unit_price
        total_amount += d.amount

    for o in order_paid:
        for d in o.detail:
            if d.book_id == book_id:
                turnover += d.amount * d.unit_price
                total_amount += d.amount
    return {
        'turnover': turnover,
        'total_amount': total_amount
    }

def stats_amount_buy_book(book_id, month=None):
    receipt_details = Receipt_detail.query.filter(Receipt_detail.book_id == book_id)
    order_paid = Order.query.filter_by(is_paid=True)

    total_amount = 0

    for r in receipt_details:
        total_amount += r.amount

    for o in order_paid:
        for d in o.detail:
            if d.book_id == book_id:
                total_amount += d.amount
    return total_amount


def category_turnover(month):
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
            res = stats_category_in_receipt(book_id=b.id, month = month)
            render_categories[c.id]['turnover'] += res['turnover']
            render_categories[c.id]['total_amount'] += res['total_amount']
            total_book += res['total_amount']
    
    for r in render_categories.values():
            r['rate'] = round(r['total_amount'] / (total_book * 0.01), 2) if r['total_amount'] else 0
    return render_categories

def book_stats(month=None):
    books = get_books()
    total_book = 0
    render_books = {}

    for b in books:
        stats_amount_buy_book(b.id)
        render_books[b.id] = {
            'name': b.name,
            'categories': convert_categories_to_str(b.category),
            'total_amount': stats_amount_buy_book(b.id)
        }
        total_book += render_books[b.id]['total_amount']

    for r in render_books.values():
        r['rate'] = r['rate'] = round(r['total_amount'] / (total_book * 0.01), 2) if r['total_amount'] else 0
    return render_books