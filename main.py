"""Create the table into a file."""


import sqlalchemy
from datamodel import Authors, Base, Books, Category
from gui import Root


def main():
    db_connection = sqlalchemy.create_engine("sqlite:///C:\\Users\\msers\\SEW\\Bookshelf\\Books.db")
    Base.metadata.create_all(db_connection)
    session_factory = sqlalchemy.orm.sessionmaker()
    session_factory.configure(bind=db_connection)
    with session_factory() as session:
        new_book = Books(book_name="Heartstopper Volume 1", book_pages=288, publish_year=2019, category_id=1, author_id=1)
        session.add(new_book)
        session.commit()
        new_book = Books(book_name="Die Welle", book_pages=192, publish_year=1997, category_id=2, author_id=2)
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

if __name__ == "__main__":
    root = Root()
    root.draw_Buttons()
    root.draw_booktable()
    root.root.mainloop()
    
