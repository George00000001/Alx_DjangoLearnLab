from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation for publication_year
    def validate_publication_year(self, Value):
        current_year = date.today().year
        if Value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return Value


class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer to show related books dynamically  
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']