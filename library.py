import json
import tkinter as tk
from tkinter import messagebox

class Book:
    def __init__(self, title, author, isbn, publication_date):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_date = publication_date
        self.checked_out = False

    def checkout(self):
        if not self.checked_out:
            self.checked_out = True
            return True
        return False

    def return_book(self):
        if self.checked_out:
            self.checked_out = False
            return True
        return False

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.checkout():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book)
            return True
        return False

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.isbn_lookup = {}

    def add_book(self, book):
        self.books.append(book)
        self.isbn_lookup[book.isbn] = book

    def remove_book(self, isbn):
        book = self.isbn_lookup.get(isbn)
        if book and book not in [b for m in self.members for b in m.borrowed_books]:
            self.books.remove(book)
            del self.isbn_lookup[isbn]
            return True
        return False

    def register_member(self, member):
        self.members.append(member)

    def checkout_book(self, member_id, isbn):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = self.isbn_lookup.get(isbn)
        if member and book and member.borrow_book(book):
            return True
        return False

    def return_book(self, member_id, isbn):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = self.isbn_lookup.get(isbn)
        if member and book and member.return_book(book):
            return True
        return False

    def search_books(self, query, by="title"):
        if by == "title":
            return [book for book in self.books if query.lower() in book.title.lower()]
        elif by == "author":
            return [book for book in self.books if query.lower() in book.author.lower()]
        elif by == "isbn":
            return [book for book in self.books if query in book.isbn]
        return []

    def sort_books(self, by="title"):
        if by == "title":
            self.books.sort(key=lambda book: book.title)
        elif by == "author":
            self.books.sort(key=lambda book: book.author)
        elif by == "publication_date":
            self.books.sort(key=lambda book: book.publication_date)

    def save_to_file(self, filename):
        data = {
            "books": [
                {
                    "title": book.title,
                    "author": book.author,
                    "isbn": book.isbn,
                    "publication_date": book.publication_date,
                    "checked_out": book.checked_out,
                }
                for book in self.books
            ],
            "members": [
                {
                    "name": member.name,
                    "member_id": member.member_id,
                    "borrowed_books": [book.isbn for book in member.borrowed_books],
                }
                for member in self.members
            ],
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)
        self.books = [
            Book(book["title"], book["author"], book["isbn"], book["publication_date"])
            for book in data["books"]
        ]
        self.isbn_lookup = {book.isbn: book for book in self.books}
        self.members = [
            Member(member["name"], member["member_id"])
            for member in data["members"]
        ]
        for member_data, member in zip(data["members"], self.members):
            member.borrowed_books = [self.isbn_lookup[isbn] for isbn in member_data["borrowed_books"]]

def main():
    library = Library()

    # Sample data
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890", "1925"))
    library.add_book(Book("1984", "George Orwell", "2345678901", "1949"))
    library.register_member(Member("Alice", "1"))
    library.register_member(Member("Bob", "2"))

    # GUI setup
    root = tk.Tk()
    root.title("Library Management System")

    def show_books():
        books = library.books
        book_list.delete(0, tk.END)
        for book in books:
            book_list.insert(tk.END, f"{book.title} by {book.author} (ISBN: {book.isbn})")

    def checkout_book():
        member_id = member_id_entry.get()
        isbn = isbn_entry.get()
        if library.checkout_book(member_id, isbn):
            messagebox.showinfo("Success", "Book checked out successfully")
        else:
            messagebox.showerror("Error", "Failed to checkout book")
        show_books()

    def return_book():
        member_id = member_id_entry.get()
        isbn = isbn_entry.get()
        if library.return_book(member_id, isbn):
            messagebox.showinfo("Success", "Book returned successfully")
        else:
            messagebox.showerror("Error", "Failed to return book")
        show_books()

    def add_book():
        title = book_title_entry.get()
        author = book_author_entry.get()
        isbn = book_isbn_entry.get()
        publication_date = book_publication_date_entry.get()
        if title and author and isbn and publication_date:
            library.add_book(Book(title, author, isbn, publication_date))
            messagebox.showinfo("Success", "Book added successfully")
            show_books()
        else:
            messagebox.showerror("Error", "Please fill in all book details")

    def add_member():
        name = member_name_entry.get()
        member_id = member_id_new_entry.get()
        if name and member_id:
            library.register_member(Member(name, member_id))
            messagebox.showinfo("Success", "Member added successfully")
        else:
            messagebox.showerror("Error", "Please fill in all member details")

    def save_data():
        library.save_to_file("library_data.json")
        messagebox.showinfo("Success", "Data saved successfully")

    def load_data():
        library.load_from_file("library_data.json")
        show_books()
        messagebox.showinfo("Success", "Data loaded successfully")

    # GUI elements
    tk.Label(root, text="Library Management System").pack()

    book_list = tk.Listbox(root)
    book_list.pack()

    tk.Label(root, text="Member ID").pack()
    member_id_entry = tk.Entry(root)
    member_id_entry.pack()

    tk.Label(root, text="ISBN").pack()
    isbn_entry = tk.Entry(root)
    isbn_entry.pack()

    tk.Button(root, text="Checkout Book", command=checkout_book).pack()
    tk.Button(root, text="Return Book", command=return_book).pack()

    tk.Label(root, text="Add New Book").pack()
    tk.Label(root, text="Title").pack()
    book_title_entry = tk.Entry(root)
    book_title_entry.pack()
    tk.Label(root, text="Author").pack()
    book_author_entry = tk.Entry(root)
    book_author_entry.pack()
    tk.Label(root, text="ISBN").pack()
    book_isbn_entry = tk.Entry(root)
    book_isbn_entry.pack()
    tk.Label(root, text="Publication Date").pack()
    book_publication_date_entry = tk.Entry(root)
    book_publication_date_entry.pack()
    tk.Button(root, text="Add Book", command=add_book).pack()

    tk.Label(root, text="Add New Member").pack()
    tk.Label(root, text="Name").pack()
    member_name_entry = tk.Entry(root)
    member_name_entry.pack()
    tk.Label(root, text="Member ID").pack()
    member_id_new_entry = tk.Entry(root)
    member_id_new_entry.pack()
    tk.Button(root, text="Add Member", command=add_member).pack()

    tk.Button(root, text="Save Data", command=save_data).pack()
    tk.Button(root, text="Load Data", command=load_data).pack()

    show_books()

    root.mainloop()

if __name__ == "__main__":
    main()
