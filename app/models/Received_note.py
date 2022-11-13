from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app import db, path

class Received_note(db.Model):
    __tablename__ = 'received_note'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

    # FOREIGN KEYS
    admin_id = Column(Integer, ForeignKey('admin.id'), nullable=False)

    # RELATIONSHIP
    received_note_book = relationship(f'{path["received_note"]}.Received_note_detail', backref='received_note', lazy=True)
    
class Received_note_detail(db.Model):
    __tablename__ = 'received_note_detail'
    __table_args__ = {'extend_existing': True}
    

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Integer, default=1, nullable=False)

    # FOREIGN KEYS
    received_note_id = Column(Integer, ForeignKey(Received_note.id), nullable=False)
    book_id = Column(Integer, ForeignKey('book.id'), nullable=False)

    