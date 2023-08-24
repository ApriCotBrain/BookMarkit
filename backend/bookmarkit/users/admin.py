"""Admin site settings of the 'users' application."""

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Representation of the User model in the admin panel."""

    list_display = (
        "pk",
        "email",
    )


admin.site.unregister(Group)
