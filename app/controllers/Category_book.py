from app.models import Book, Category

def get_book_by_id(id):
    return Book.query.get(id)

def get_books(from_price=None, to_price=None, kw=None, category=None):
    product = Book.query

    if (from_price):

        product = product.filter(Book.price >= from_price)
    if (to_price):
        product = product.filter(Book.price <= to_price)

    if (kw):
        product = product.filter(Book.name.contains(kw))
    
    if (category):
        product = product.all()
        newProduct = []
        for p in product:
            for c in p.category:
                if c.id == int(category):
                    newProduct.append(p)
        return newProduct
    
    return product.all()

def get_categories():
    return Category.query.all()

def convert_categories_to_str(categories):
    newList = []
    for c in categories:
        newList.append(c.name)
    
    return ','.join(newList)