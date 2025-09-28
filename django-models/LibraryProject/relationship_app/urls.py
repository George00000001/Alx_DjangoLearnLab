from django.urls import path
from .views import list_books, LibraryDetailView
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', list_books, name='books'),
    path('library/', LibraryDetailView.as_view(), name='library'),
]

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Registration (custom view)
    path("register/", views.register_view, name="register"),

    # Login & Logout using Django's built-in views
    path(
        "login/",
        LoginView.as_view(template_name="relationship_app/login.html"),
        name="login"
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="relationship_app/logout.html"),
        name="logout"
    ),
]

urlpatterns = [
    # Authentication
    path("register/", views.register_view, name="register"),
    path(
        "login/",
        LoginView.as_view(template_name="relationship_app/login.html"),
        name="login"
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="relationship_app/logout.html"),
        name="logout"
    ),

    # Role-based views
    path("admin-dashboard/", views.admin_view, name="admin_view"),
    path("librarian-dashboard/", views.librarian_view, name="librarian_view"),
    path("member-dashboard/", views.member_view, name="member_view"),
]

urlpatterns = [
    # Book permission views
    path("books/add/", views.add_book, name="add_book"),
    path("books/<int:book_id>/edit/", views.edit_book, name="edit_book"),
    path("books/<int:book_id>/delete/", views.delete_book, name="delete_book"),
]