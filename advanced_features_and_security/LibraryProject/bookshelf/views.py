from django.shortcuts import render, redirect
from .forms import ExampleForm

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {"books": books})

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    return HttpResponse("Form to create a book here.")

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return HttpResponse(f"Editing book: {book.title}")

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return HttpResponse("Book deleted.")


def form_example_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")  # replace with your actual URL name
    else:
        form = ExampleForm()
    return render(request, "bookshelf/form_example.html", {"form": form})