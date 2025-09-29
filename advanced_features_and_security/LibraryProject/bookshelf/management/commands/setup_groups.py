from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book  # replace with your actual model

class Command(BaseCommand):
    help = "Set up default groups and permissions"

    def handle(self, *args, **kwargs):
        content_type = ContentType.objects.get_for_model(Book)

        # Permissions that should already exist in Book.Meta.permissions
        perms = {
            "can_view": "Can view book",
            "can_create": "Can create book",
            "can_edit": "Can edit book",
            "can_delete": "Can delete book",
        }

        # Create groups
        editors, _ = Group.objects.get_or_create(name="Editors")
        viewers, _ = Group.objects.get_or_create(name="Viewers")
        admins, _ = Group.objects.get_or_create(name="Admins")

        # Assign permissions to groups
        for codename, name in perms.items():
            try:
                permission = Permission.objects.get(
                    codename=codename, content_type=content_type
                )
            except Permission.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Permission {codename} not found"))
                continue

            if codename in ["can_edit", "can_create"]:
                editors.permissions.add(permission)

            if codename == "can_view":
                viewers.permissions.add(permission)

            admins.permissions.add(permission)

        self.stdout.write(self.style.SUCCESS("✅ Groups and permissions set up successfully!"))
