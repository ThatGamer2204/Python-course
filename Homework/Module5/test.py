class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            print(f"'{self.title}' is already borrowed.")
        else:
            self.is_borrowed = True
            print(f"You borrowed '{self.title}'.")

    def return_book(self):
        if not self.is_borrowed:
            print(f"'{self.title}' wasn't borrowed.")
        else:
            self.is_borrowed = False
            print(f"You returned '{self.title}'.")

    def __str__(self):
        if self.is_borrowed:
            status = "Borrowed"
        else:
            status = "Available"

        return f"{self.title} by {self.author} [{status}]"



book1 = Book("Python Crash Course", "Eric Matthes")
book2 = Book("The Hobbit", "J.R.R. Tolkien")
book3 = Book("1984", "George Orwell")

print("=" * 42)
print("         📚  LIBRARY SYSTEM")
print("=" * 42)

print(book1)
print(book2)
print(book3)

book1.borrow()
book2.borrow()

book1.borrow()

book1.return_book()

book3.return_book()

print(book1)
print(book2)
print(book3)