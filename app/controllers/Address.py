from app.models import Address
from flask_login import current_user
from app import db


def add_address(city_id, district_id, ward_id, address):
        
    address_model = Address.query.filter(Address.customer_id == current_user.id).first()


    if address_model:
      db.session.delete(address_model)  
      db.session.commit()
    new_address = Address(customer_id=current_user.id, city_id=city_id, district_id=district_id, ward_id=ward_id, address=address)
    db.session.add(new_address)
    db.session.commit()
        
def get_last_address():
    address =  Address.query.all()

    return address[-1]