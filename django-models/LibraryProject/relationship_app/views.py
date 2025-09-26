from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    book_info = [f"{book.title} by {book.author.name}" for book in books]
    context = {'book_list' : books}
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add all books in this library to the context
        context['books'] = self.object.books.all()
        return context 