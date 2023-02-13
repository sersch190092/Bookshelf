from datamodel import Authors, Base, Books, Category
from functions import Functions


def test_001_insert_into_table():
    function = Functions()
    count_before_insert = function.session.query(Books).count()
    function.create_book("Erebos", 509, 2011, 2, 2)
    count_temp = function.session.query(Books).count()
    assert (count_before_insert+1 == count_temp)
