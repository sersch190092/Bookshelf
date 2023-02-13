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
        btn_Books = tk.Button(text="Books", command=self.draw_booktable)
        btn_Books.grid(column=0, sticky=tk.E, row=0, padx=2, pady=2)

        btn_Authors = tk.Button(text="Authors", command=self.draw_authortable)
        btn_Authors.grid(column=1, row=0, padx=2, pady=2)

        btn_Categories = tk.Button(text="Categories", command=self.draw_categorytable)
        btn_Categories.grid(column=2, sticky=tk.W, row=0, padx=2, pady=2)

        btn_Add = tk.Button(text="+", command=self.draw_save)
        btn_Add.grid(column=0, sticky=tk.E, row=1, padx=2, pady=2)

        btn_Delete = tk.Button(text="-")
        btn_Delete.grid(column=1, row=1, padx=2, pady=2)

    def draw_booktable(self):
        table_books = ttk.Treeview(self.root, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', height=5)
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
        table_author = ttk.Treeview(self.root, column=("c1", "c2", "c3"), show='headings', height=5)
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
        table_category = ttk.Treeview(self.root, column=("c1", "c2"), show='headings', height=5)
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

    def draw_save(self):
        top = Toplevel(self.root)
        top.geometry("750x250")

        functions1 = Functions()

        label1 = tk.Label(top, text="Enter new book!")
        label1.grid(column=0, sticky=tk.E, row=0, padx=2, pady=2)

        entry_name = tk.Entry(top, width=25)
        entry_name.grid(column=0, sticky=tk.E, row=1, padx=2, pady=2)
        entry_name.insert(0, "Book Name")

        entry_pages = tk.Entry(top, width=25)
        entry_pages.grid(column=1, row=1, padx=2, pady=2)
        entry_pages.insert(0, "Page Number")

        entry_publish_year = tk.Entry(top, width=25)
        entry_publish_year.grid(column=2, row=1, padx=2, pady=2)
        entry_publish_year.insert(0, "Publish Year")

        entry_category = tk.Entry(top, width=25)
        entry_category.grid(column=3, row=1, padx=2, pady=2)
        entry_category.insert(0, "Category ID")

        entry_author = tk.Entry(top, width=25)
        entry_author.grid(column=4, row=1, padx=2, pady=2)
        entry_author.insert(0, "Author ID")

        btn_store = tk.Button(top, text="Store", command=functions1.create_book(entry_name, entry_pages, entry_publish_year, entry_category, entry_author))
        btn_store.grid(column=0, sticky=tk.W, row=2, padx=2, pady=2)

