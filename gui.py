import tkinter as tk
from tkinter import *
from tkinter import ttk
from functions import Functions


class Root():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bibliothek")
        self.root.minsize(500, 400)
        self.root.columnconfigure((0, 1, 2, 3, 4), weight=0)
        self.root.rowconfigure((0, 1), weight=0)
        self.root.rowconfigure(2, weight=1)

    def draw_Buttons(self):
        btn_Books = tk.Button(text="Books", command=self.draw_booktable, width=15)
        btn_Books.grid(column=0, sticky=tk.E, row=0, padx=2, pady=2)

        btn_Authors = tk.Button(text="Authors", command=self.draw_authortable, width=15)
        btn_Authors.grid(column=1, row=0, padx=2, pady=2)

        btn_Categories = tk.Button(text="Categories", command=self.draw_categorytable, width=15)
        btn_Categories.grid(column=2, sticky=tk.W, row=0, padx=2, pady=2)

        btn_AddBook = tk.Button(text="+", command=self.draw_saveBook, width=15)
        btn_AddBook.grid(column=0, sticky=tk.E, row=1, padx=2, pady=2)

        btn_AddAuthor = tk.Button(text="+", command=self.draw_AuthorStore, width=15)
        btn_AddAuthor.grid(column=1, row=1, padx=2, pady=2)

        btn_AddCategory = tk.Button(text="+", command=self.draw_CategoryStore, width=15)
        btn_AddCategory.grid(column=2, sticky=tk.W, row=1, padx=2, pady=2)

    def draw_booktable(self):
        table_books = ttk.Treeview(self.root, column=("c1", "c2", "c3", "c4", "c5", "c6"),
                                   show='headings', height=13)
        table_books.heading("#1", anchor=CENTER)
        table_books.heading("#1", text="ID")
        table_books.heading("#2", anchor=CENTER)
        table_books.heading("#2", text="Book Name")
        table_books.heading("#3", anchor=CENTER)
        table_books.heading("#3", text="Pages")
        table_books.heading("#4", anchor=CENTER)
        table_books.heading("#4", text="Publish Year")
        table_books.heading("#5", anchor=CENTER)
        table_books.heading("#5", text="Category")
        table_books.heading("#6", anchor=CENTER)
        table_books.heading("#6", text="Author ID")

        functions1 = Functions()
        books_count = functions1.get_book_count()

        books = functions1.get_books()
        for Book_rndm in range(books_count):
            book = books[Book_rndm]
            category_name = functions1.get_category_name(book.category_id)
            table_books.insert('',
                               'end',
                               text="1",
                               values=(book.book_id,
                                       book.book_name,
                                       book.book_pages,
                                       book.publish_year,
                                       category_name,
                                       book.author_id))
        table_books.grid(column=0, sticky=tk.EW, row=2, padx=2, pady=1, columnspan=3)

    def draw_authortable(self):
        table_author = ttk.Treeview(self.root, column=("c1", "c2", "c3"), show='headings', height=13)
        table_author.heading("#1", anchor=CENTER)
        table_author.heading("#1", text="ID")
        table_author.heading("#2", anchor=CENTER)
        table_author.heading("#2", text="First Name")
        table_author.heading("#3", anchor=CENTER)
        table_author.heading("#3", text="Last Name")

        functions1 = Functions()
        author_count = functions1.get_author_count()

        authors = functions1.get_authors()
        for Author_rndm in range(author_count):
            author = authors[Author_rndm]
            table_author.insert('',
                                'end',
                                text="1",
                                values=(author.author_id,
                                        author.first_name,
                                        author.last_name))
        table_author.grid(column=0, sticky=tk.EW, row=2, padx=2, pady=1, columnspan=3)

    def draw_categorytable(self):
        table_category = ttk.Treeview(self.root, column=("c1", "c2"), show='headings', height=13)
        table_category.heading("#1", anchor=CENTER)
        table_category.heading("#1", text="ID")
        table_category.heading("#2", anchor=CENTER)
        table_category.heading("#2", text="Name")

        functions1 = Functions()
        category_count = functions1.get_category_count()

        categories = functions1.get_categories()
        for category_rndm in range(category_count):
            category = categories[category_rndm]
            table_category.insert('',
                                  'end',
                                  text="1",
                                  values=(category.category_id,
                                          category.name))
        table_category.grid(column=0, sticky=tk.EW, row=2, padx=2, pady=1, columnspan=3)

    def save_data(self):
        ttk.label.config(text=ttk.entry.get())

    def draw_saveBook(self):
        top = Toplevel(self.root)
        top.geometry("750x250")

        label1 = tk.Label(top, text="Enter new book!")
        label1.grid(column=0, sticky=tk.E, row=0, padx=2, pady=2)

        self.entry_name = tk.Entry(top, width=25)
        self.entry_name.grid(column=0, sticky=tk.E, row=1, padx=2, pady=2)
        self.entry_name.insert(0, "Book Name")

        self.entry_pages = tk.Entry(top, width=25)
        self.entry_pages.grid(column=1, row=1, padx=2, pady=2)
        self.entry_pages.insert(0, "Page Number")

        self.entry_publish_year = tk.Entry(top, width=25)
        self.entry_publish_year.grid(column=2, row=1, padx=2, pady=2)
        self.entry_publish_year.insert(0, "Publish Year")

        self.entry_category = tk.Entry(top, width=25)
        self.entry_category.grid(column=3, row=1, padx=2, pady=2)
        self.entry_category.insert(0, "Category ID")

        self.entry_author = tk.Entry(top, width=25)
        self.entry_author.grid(column=4, row=1, padx=2, pady=2)
        self.entry_author.insert(0, "Author ID")

        btn_store = tk.Button(top, text="Store", command=self.create_book_entry)
        btn_store.grid(column=0, sticky=tk.E, row=2, padx=2, pady=2)

    def create_book_entry(self):
        functions1 = Functions()
        functions1.create_book(self.entry_name.get(),
                               self.entry_pages.get(),
                               self.entry_publish_year.get(),
                               self.entry_category.get(),
                               self.entry_author.get())
        self.draw_booktable()

    def remove_book(self):
        remove_win = Toplevel(self.root)
        remove_win.geometry("100x100")

        label = tk.Label(remove_win, text="Book name to be removed:")
        label.grid(column=0, sticky=tk.E, row=0, padx=2, pady=2)

        self.book_name = tk.Entry(remove_win, width=10)
        self.entry_bookname.grid(column=0, sticky=tk.E, row=1, padx=2, pady=2)
        self.entry_bookname.insert(0, "Book Name")

        btn_remove = tk.Button(remove_win, text="Delete", command=self.remove_book_e)
        btn_remove.grid(column=0, sticky=tk.W, row=2, padx=2, pady=2)

    def remove_book_e(self):
        functions1 = Functions()
        functions1.delete_book(self.entry_bookname.get())
        self.draw_authortable()

    def draw_AuthorStore(self):
        top = Toplevel(self.root)
        top.geometry("750x250")

        label1 = tk.Label(top, text="Enter new author!")
        label1.grid(column=0, sticky=tk.E, row=0, padx=2, pady=2)

        self.entry_firstname = tk.Entry(top, width=25)
        self.entry_firstname.grid(column=0, sticky=tk.E, row=1, padx=2, pady=2)
        self.entry_firstname.insert(0, "First Name")

        self.entry_lastname = tk.Entry(top, width=25)
        self.entry_lastname.grid(column=1, row=1, padx=2, pady=2)
        self.entry_lastname.insert(0, "Last Name")

        btn_store = tk.Button(top, text="Store", command=self.create_author_entry)
        btn_store.grid(column=0, sticky=tk.W, row=2, padx=2, pady=2)

    def create_author_entry(self):
        functions1 = Functions()
        functions1.create_author(self.entry_firstname.get(),
                                 self.entry_lastname.get())
        self.draw_authortable()

    def draw_CategoryStore(self):
        top = Toplevel(self.root)
        top.geometry("750x250")

        label1 = tk.Label(top, text="Enter new category!")
        label1.grid(column=0, sticky=tk.E, row=0, padx=2, pady=2)

        self.entry_name = tk.Entry(top, width=25)
        self.entry_name.grid(column=0, sticky=tk.E, row=1, padx=2, pady=2)
        self.entry_name.insert(0, "Name")

        btn_store = tk.Button(top, text="Store", command=self.create_category_entry)
        btn_store.grid(column=0, sticky=tk.W, row=2, padx=2, pady=2)

    def create_category_entry(self):
        functions1 = Functions()
        functions1.create_category(self.entry_name.get())
        self.draw_categorytable()
