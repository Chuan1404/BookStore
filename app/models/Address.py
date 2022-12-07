from sqlalchemy import Column, Integer, ForeignKey, String
from app import db

class Address(db.Model):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True, autoincrement=True)

    city_id = Column(Integer, default=1)
    district_id = Column(Integer, default=1)
    ward_id = Column(Integer, default=1)
    address = Column(String(100))

    customner_id = Column(Integer, ForeignKey('user.id'), nullable=False)