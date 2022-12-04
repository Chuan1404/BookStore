from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from datetime import datetime
from app import db

class Note(db.Model):
    __tablename__ = 'note'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    import_at = Column(DateTime, default=datetime.now().date())
    created_at = Column(DateTime, default=datetime.now().date())
    updated_at = Column(DateTime, default=datetime.now().date())

    # FOREIGN KEYS
    admin_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    
    # RELATIONSHIP
    note_book = relationship('Note_detail', backref='note', lazy=True)

    def __str__(self):
        return self.name

class Note_detail(db.Model):
    __tablename__ = 'note_detail'
    

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Integer, default=1, nullable=False)

    # FOREIGN KEYS
    note_id = Column(Integer, ForeignKey(Note.id), nullable=False)
    book_id = Column(Integer, ForeignKey('book.id'), nullable=False)

    # def __str__(self):
    #     return f'Note-{self.note_id} and Book-{self.book_id}'