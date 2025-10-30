# Name: Krittitee Chaisang #  Student ID: 6810545441
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
class Library:
    def __init__(self):
        self.__books = []
        
    def add_book(self, title, author):
        self.__books.append(Book(title, author))
        
    def get_book_count(self):
        return len(self.__books)
    
    def display_books(self):
        pepig = []
        for book in self.__books:
            pepig.append(f'{book.title} by {book.author}')
        return pepig
 

Lib=Library()

while True:
    cmd = input("Command (add/view/count/exit): ")
    if cmd == 'exit':
        print("Goodbye.")
        break
    if cmd == 'add':
        title = input("Enter title: ")
        author = input("Enter author: ")
        Lib.add_book(title,author)
        print("Book added.")
    if cmd == 'view':
        print("--- Library Holdings ---")
        for book in Lib.display_books():
            print(book)