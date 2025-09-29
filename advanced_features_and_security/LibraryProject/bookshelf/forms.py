from django import forms
from .models import Book

# Example form for creating/updating a Book
class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publication_date", "isbn"]

    # Extra validation example (optional)
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if "badword" in title.lower():
            raise forms.ValidationError("Inappropriate word detected in title.")
        return title
