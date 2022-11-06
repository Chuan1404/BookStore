from app import app, db
from . import User, PhieuNhapSach



with app.app_context():
    db.create_all()