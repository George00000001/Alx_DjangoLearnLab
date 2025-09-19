from django.contrib import admin
from .models import Book

# Simple registration
# admin.site.register(Book)

# Better: Custom admin class
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Show these fields in the list view
    list_display = ("title", "author", "publication_year")

    # Add filters in the right sidebar
    list_filter = ("publication_year", "author")

    # Enable search by title or author
    search_fields = ("title", "author")
