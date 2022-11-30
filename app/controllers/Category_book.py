from app.models import Book, Category

def get_book_by_id(id):
    return Book.query.get(id)

def get_books():
    return Book.query.all()

def get_categories():
    return Category.query.all()

def convert_categories_to_str(book):
    strs = []
    if book.category:
        for category in book.category:
            strs.append(category.__str__())
        return ','.join(strs)
    else:
        return ''
