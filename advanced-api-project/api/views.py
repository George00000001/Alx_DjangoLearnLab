from django.shortcuts import render
from rest_framework import generics, filters
from .models import Book, Author
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django_filters import rest_framework


# Create your views here.

class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']  # Filter by exact match
    search_fields = ['title', 'author__name']  # Text search
    ordering_fields = ['title', 'publication_year']  # Sortable fields
    ordering = ['title']  # Default ordering

    def get_queryset(self):
        # Optionally limit results to user's books if authenticated
        if self.request.user.is_authenticated:
            return Book.objects.filter(created_by=self.request.user)
        return Book.objects.none()
    
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
       if self.request.user != serializer.instance.created_by:
        raise PermissionDenied("You do not have permission to edit this book.")
        serializer.save()
        
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]