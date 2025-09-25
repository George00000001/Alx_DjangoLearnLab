from bookshelf.models import Book

retrieved_book = Book.objects.get(id=book.id)
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)

Django Basics Jane Doe 2023