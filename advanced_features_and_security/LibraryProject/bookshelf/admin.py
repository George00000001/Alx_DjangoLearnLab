from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "published_date"]
    list_filter = ["author", "published_date"]
admin.site.register(Book, BookAdmin)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # you can customize the admin display here:
    list_display = ["username", "email", "is_staff", "is_active"]
    search_fields = ["username", "email"]
    ordering = ["username"]


admin.site.register(CustomUser, CustomUserAdmin)