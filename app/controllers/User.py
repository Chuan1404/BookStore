from app import db

from app.models.User import Customer, User_role, Admin, Warehouse_manager, Staff

def get_user_by_id(id):
    return Customer.query.get(id)

def add_user(username, name, email, phone_number, password, role):

    if role.__eq__(User_role.CUSTOMMER):
        user = Customer(username=username, name=name, email=email, phone_number=phone_number, password=password)
    elif role.__eq__(User_role.ADMIN):
        user = Admin(username=username, name=name, email=email, phone_number=phone_number, password=password)
    elif role.__eq__(User_role.STAFF):
        user = Staff(username=username, name=name, email=email, phone_number=phone_number, password=password)
    elif role.__eq__(User_role.WAREHOUSE_MANAGER):
        user = Warehouse_manager(username=username, name=name, email=email, phone_number=phone_number, password=password)

    if user:
        db.session.add(user)
        db.session.commit()
        
