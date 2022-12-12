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
    note = Note.query.get(note_id)
    note_details = note.detail

    books = []
    for detail in note_details:
        books.append({
            'book': get_book_by_id(detail.book_id),
            'amount': detail.amount
        })
    if books:
        return {
            'status': 1,
            'data': {
                'note_id': note_id,
                'is_imported': note.is_imported,
                'books': books
            }
        }
    else: 
        return {
            'status': 0,
            'err': "Not found"
        }
    
def data_import_page(date=datetime.now().date()):
    note = get_note_by_date(date)
    if note.get('status') == 1:
        res = get_books_in_note_detail(note.get('data').id)
        if res.get('status') == 1:
            return res.get("data")
        else:
            return 0
    else:
        return 0

