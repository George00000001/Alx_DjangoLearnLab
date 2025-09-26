from relationship_app.models import Author, Book, Library, Librarian

author_name = "Author Name"
author = Author.objects.get(name=author_name)
library_name = "Library Name"

# Books by author
books_by_author = Book.objects.filter(author=author_name)
for book in books_by_author:
    print(book.title)

# Books in library
library = Library.objects.get(name=library_name)
book_in_library= Library.books.all()
for book in book_in_library:
    print(book.title)

# Librarian for a library
librarian = library.librarian
librarian_in_library = print(librarian.name)
