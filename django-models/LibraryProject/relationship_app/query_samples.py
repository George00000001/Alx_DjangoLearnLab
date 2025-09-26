from relationship_app.models import Author, Book, Library, Librarian

author = Author.objects.get(name="Author Name")
name = "Library Name"

# Books by author
books_by_author = Book.objects.filter(author=author)
for book in books_by_author:
    print(book.title)

# Books in library
library = Library.objects.get(name=name)
book_in_library= Library.book_set.all()
for book in book_in_library:
    print(book.title)

# Librarian for a library
librarian = library.librarian
librarian_in_library = print(librarian.name)
