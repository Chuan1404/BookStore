from app.models import Book, Category


def get_books():
    return Book.query.all()

def get_categories():
    return Category.query.all()
