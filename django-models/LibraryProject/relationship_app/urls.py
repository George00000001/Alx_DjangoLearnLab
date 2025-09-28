from django.urls import path
from .views import list_books, LibraryDetailView

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

