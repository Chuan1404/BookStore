from app.models import Note, Note_detail
from app.utils import *
from datetime import datetime
from app.controllers import *

def get_note_by_date(date=datetime.now().date()):
    note = Note.query.filter(Note.import_at == date).first()
    if note:
        return {
            "status": 1,
            "data": note,
        }
    else:
        return {
            "status": 0,
            "err": "Not found"
        }

def get_books_in_note_detail(note_id):
    note_details = Note_detail.query.filter(Note_detail.note_id == note_id).all()
    books = []
    for detail in note_details:
        books.append({
            'book': get_book_by_id(detail.book_id),
            'amount': detail.amount
        })
    if books:
        return {
            'status': 1,
            'data': books
        }
    else: 
        return {
            'status': 0,
            'err': "Not found"
        }
    
def data_import_page(date=datetime.now().date()):
    note = get_note_by_date(date)

    if note.get('status') == 1:
        books = get_books_in_note_detail(note.get('data').id)
        if books.get('status') == 1:
            return books.get("data")
        else:
            return 0
    else:
        return 0