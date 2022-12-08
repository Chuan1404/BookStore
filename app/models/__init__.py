from app import app, db

from app.models.User import *

from app.models.Rule import * 

from app.models.Category_book import *

from app.models.Receipt import *

from app.models.Note import *

from app.models.Address import *

from app.models.Admin import *



with app.app_context():
    db.create_all()