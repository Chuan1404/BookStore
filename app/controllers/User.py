from app.models.User import User 

def get_user_by_id(id):
    return User.query.get(id)