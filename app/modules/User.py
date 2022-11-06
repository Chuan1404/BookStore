from sqlalchemy import Column, Integer
from app import app, db

class User(db.Model):

    id = Column(Integer, primary_key=True, autoincrement=True)

with app.app_context():
    db.create_all()
