import sqlalchemy

from datamodel import Authors, Base, Books, Category
from sqlalchemy.orm import sessionmaker

class Functions:
    """Run Main function."""

    def __init__(self):
        db_connection = sqlalchemy.create_engine("sqlite:///C:\\Users\\msers\\SEW\\Bookshelf\\Books.db")
        Base.metadata.create_all(bind=db_connection)
        Session = sessionmaker(bind=db_connection)
        self.session = Session()

    def create_book(self, Book_name, Book_pages, Publish_year, Category_name, Author_id):
        Category = self.session.query(Category).filter_by(name=Category_name).first()
        if Category is None:
            self.create_category(Category_name)
        else:
            category_id = self.session.query(Category).filter_by(name=Category_name).first()
            new_book = Books(book_name=Book_name, book_pages=Book_pages, publish_year=Publish_year,category_id=category_id.category_id, author_id=Author_id)
            self.session.add(new_book)
            self.session.commit()

    def create_author(self, First_name, Last_name):
        new_author = Authors(first_name=First_name, last_name=Last_name)
        self.session.add(new_author)
        self.session.commit()

    def create_category(self, Name):
        new_category = Category(name=Name)
        self.session.add(new_category)
        self.session.commit()

    def delete_book(self, Book_name):
        self.session.query(Books).filter_by().delete()

    def delete_author(self, author_id):
        self.session.query(Authors).filter_by().delete()

    def get_book_count(self):
        value = self.session.query(Books).count()
        return value

    def get_books(self):
        books = self.session.query(Books).all()
        return books

    def get_category_name(self, category):
        category_name = self.session.query(Category).filter_by(category_id=category).first()
        return category_name.name

    def get_author_count(self):
        value = self.session.query(Authors).count()
        return value

    def get_authors(self):
        authors = self.session.query(Authors).all()
        return authors

    def get_category_count(self):
        value = self.session.query(Category).count()
        return value

    def get_categories(self):
        categories = self.session.query(Category).all()
        return categories
