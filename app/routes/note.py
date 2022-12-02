from app import app, db
from app.controllers import get_books_in_note_detail

from flask import request
import json

@app.route('/api/submit-note', methods=['POST'])
def submit_note():
    note_id = request.json['note_id']
    res = get_books_in_note_detail(note_id)

    if res.get('status'):
        for book in res.get('data').get('books'):
            book.get('book').amount += book.get('amount')
        
        db.session.commit()


    return json.dumps({
        'status': 1
    })