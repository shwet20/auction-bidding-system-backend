from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


class AppUserAdmin(UserAdmin):
    list_display = (
        "id",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "last_login",
        "role",
        "date_joined",
    )
    list_filter = ("is_active", "is_superuser", "role")
    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("id",)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "role")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(User, AppUserAdmin)
