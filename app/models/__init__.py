from app import app, db

from app.models.User import *

from app.models.Rule import * 

from app.models.Category_book import *

from app.models.Receipt import *

from app.models.Received_note import *


with app.app_context():
    db.create_all()