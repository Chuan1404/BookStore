from app.models import Address
from flask_login import current_user
from app import db


def add_address(city_id, district_id, ward_id, address):
    compare_address = ''
    if compare_address == address:
        compare_address = None
        
    address_model = Address.query.filter(Address.customer_id == current_user.id, Address.city_id ==
                                   city_id, Address.district_id == district_id, Address.ward_id == ward_id,
                                   Address.address == compare_address).first()


    if not address_model:
        new_address = Address(customer_id=current_user.id, city_id=city_id, district_id=district_id, ward_id=ward_id, address=address)
        db.session.add(new_address)
        db.session.commit()
