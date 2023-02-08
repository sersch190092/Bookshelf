"""Model of database is declared here."""

import sqlalchemy
import sqlalchemy.ext.declarative



Base = sqlalchemy.ext.declarative.declarative_base()


class Books(Base):
    """Create Book representation."""

    __tablename__ = "Books"
    book_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    book_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    book_pages = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    publish_year = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    category_id = sqlalchemy.Column(sqlalchemy.ForeignKey(
                                    "Category.category_id"),
                                    nullable=False)


class Authors(Base):
    """Create Authors representation."""

    __tablename__ = "Authors"
    author_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    first_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    last_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)


class Category(Base):
    """Create Category representation."""

    __tablename__ = "Category"
    category_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)


class Book_author(Base):
    """Create crosstable for book and authors."""

    __tablename__ = "book_author"
    book_author_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    book_id = sqlalchemy.Column(sqlalchemy.ForeignKey("Books.book_id"),
                                nullable=False)
    author_id = sqlalchemy.Column(sqlalchemy.ForeignKey("Authors.author_id"),
                                  nullable=False)
