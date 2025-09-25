from bookshelf.models import Book

book = Book.objects.create(title="Django Basics", author="George Orwell", publication_year=2023)

print(book)
Book object (2)