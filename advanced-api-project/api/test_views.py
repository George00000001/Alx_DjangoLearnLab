"""
### Testing Strategy

- **Framework:** Django’s built-in unittest via `rest_framework.test.APITestCase`
- **Focus Areas:**
  - CRUD operations (create, update, delete, retrieve)
  - Filtering (`?author=1`)
  - Searching (`?search=title`)
  - Ordering (`?ordering=publication_year`)
  - Permissions (authenticated vs unauthenticated)
- **Command to Run Tests:**
  ```bash
  python manage.py test api
"""
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Book, Author


class BookAPITests(APITestCase):
    """Unit tests for Book API endpoints."""

    def setUp(self):
        # Create users
        self.user = User.objects.create_user(username="george", password="pass123")
        self.other_user = User.objects.create_user(username="other", password="pass123")

        # Create authors
        self.author1 = Author.objects.create(name="George Orwell")
        self.author2 = Author.objects.create(name="J.K. Rowling")

        # Create sample books
        self.book1 = Book.objects.create(
            title="1984", author=self.author1, publication_year=1949, created_by=self.user
        )
        self.book2 = Book.objects.create(
            title="Harry Potter", author=self.author2, publication_year=1997, created_by=self.user
        )

        # Initialize client
        self.client = APIClient()

        # Endpoints
        self.list_url = "/api/books/"
        self.create_url = "/api/books/create/"
        self.detail_url = f"/api/books/{self.book1.id}/"
        self.update_url = f"/api/books/{self.book1.id}/update/"
        self.delete_url = f"/api/books/{self.book1.id}/delete/"

    # ---------- CRUD TESTS ----------

    def test_list_books_unauthenticated(self):
        """Unauthenticated users can view the book list (read-only)."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book_authenticated(self):
        """Authenticated user can create a new book."""
        self.client.login(username="george", password="pass123")
        data = {
            "title": "Animal Farm",
            "author": self.author1.id,
            "publication_year": 1945
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Unauthenticated users cannot create a book."""
        data = {
            "title": "Unauthorized Book",
            "author": self.author1.id,
            "publication_year": 2024
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_own_book(self):
        """User can update their own book."""
        self.client.login(username="george", password="pass123")
        data = {"title": "1984 - Updated"}
        response = self.client.put(self.update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "1984 - Updated")

    def test_cannot_update_others_book(self):
        """User cannot update a book created by another user."""
        self.client.login(username="other", password="pass123")
        data = {"title": "Malicious Edit"}
        response = self.client.put(self.update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book(self):
        """Authenticated user can delete their own book."""
        self.client.login(username="george", password="pass123")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ---------- FILTERING, SEARCHING, ORDERING TESTS ----------

    def test_filter_books_by_author(self):
        """User can filter books by author."""
        self.client.login(username="george", password="pass123")
        response = self.client.get(f"{self.list_url}?author={self.author1.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(book["author"] == self.author1.id for book in response.data))

    def test_search_books_by_title(self):
        """User can search books by title."""
        self.client.login(username="george", password="pass123")
        response = self.client.get(f"{self.list_url}?search=Harry")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Harry" in book["title"] for book in response.data))

    def test_order_books_by_publication_year(self):
        """User can order books by publication year."""
        self.client.login(username="george", password="pass123")
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))
