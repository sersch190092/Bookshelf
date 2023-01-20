"""Create the table into a file."""

import sqlalchemy

from database import Base, Books, Authors


def main():
    """Run Main function."""
    db_connection = sqlalchemy.create_engine("sqlite:///C:\\Users\\msers\\SEW\\Bookshelf\\Books.db")
    Base.metadata.create_all(db_connection)
    session_factory = sqlalchemy.orm.sessionmaker()
    session_factory.configure(bind=db_connection)
    with session_factory() as session:
        new_book = Books(book_name="Heartstopper Volume 1", author_id=1, book_pages=288)
        new_author = Authors(first_name="Alice", last_name="Oseman")
        session.add(new_author, new_book)
        session.commit()


if __name__ == "__main__":
    main()
