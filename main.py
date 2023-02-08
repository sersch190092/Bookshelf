"""Create the table into a file."""

import sqlalchemy

from datamodel import Authors, Base, Book_author, Books, Category


def main(self):
    """Run Main function."""
    db_connection = sqlalchemy.create_engine("sqlite:///C:\\Users\\msers\\SEW\\Bookshelf\\Books.db")
    Base.metadata.create_all(db_connection)
    self.session_factory = sqlalchemy.orm.sessionmaker()
    self.session_factory.configure(bind=db_connection)
    with self.session_factory() as session:
        new_book = Books(book_name="Heartstopper Volume 1", book_pages=288, publish_year=2019, category_id=1)
        session.add(new_book)
        session.commit()
        new_book = Books(book_name="Die Welle", book_pages=192, publish_year=1997, category_id=2 )
        session.add(new_book)
        session.commit()

        new_author = Authors(first_name="Alice", last_name="Oseman")
        session.add(new_author)
        session.commit()
        new_author = Authors(first_name="Morton", last_name="Rhue")
        session.add(new_author)
        session.commit()

        new_category = Category(name="Romance")
        session.add(new_category)
        session.commit()
        new_category = Category(name="Roman")
        session.add(new_category)
        session.commit()

    def create_book(self, Book_name, Book_pages, Publish_year, Category_id):
        with self.session_factory() as session:
            new_book = Books(book_name = Book_name, book_pages=Book_pages, publish_year=Publish_year,category_id=Category_id)
            session.add(new_book)
            session.commit()

    def create_author(self, First_name, Last_name):
        with self.session_factory() as session:
            new_author = Authors(first_name=First_name, last_name=Last_name)
            session.add(new_author)
            session.commit()

    def create_category(self, Name):
        with self.session_factory() as session:
            new_category = Category(name=Name)
            session.add(new_category)
            session.commit()

    def delete_book(self, Book_name):
        session = self.session_factory()
        session.query(Books).filter_by().delete()

    def delete_author(self, author_id):
        






if __name__ == "__main__":
    main()
