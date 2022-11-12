from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app import db

class Book_received_note(db.Model):
    __tablename__ = 'book_received_note'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

    # FOREIGN KEYS
    admin_id = Column(Integer, ForeignKey('admin.id'), nullable=False)

    # RELATIONSHIP
    details = relationship('book_received_note_detail', backref='received_note_detail')
    
class Book_received_note_detail(db.Model):
    __tablename__ = 'book_received_note_detail'

    amount = Column(Integer, default=1, nullable=False)

    # FOREIGN KEYS
    received_note_id = Column(Integer, ForeignKey(Book_received_note.id), nullable=False)
    book_id = Column(Integer, ForeignKey('Book.id'), nullable=False)

    
