from bookshelf.models import Book

retrieved_book = Book.objects.get(id=book.id)
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)

1984 George Orwell 2023