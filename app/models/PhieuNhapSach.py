from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from app import db

class PhieuNhapSach(db.Model):
    __tablename__ = 'phieu_nhap_sach'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

    # FOREIGN KEYS
    admin_id = Column(Integer, ForeignKey('admin.id'), nullable=False)
    

    
