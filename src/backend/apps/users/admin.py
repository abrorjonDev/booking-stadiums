from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (_('User Info'), 
            {'fields': (
                "phone_number",
            )
        }),
        (_('Status/Groups/Permissions'), 
            {'fields': (
                'is_active', 
                'is_staff', 
                'is_superuser',
                'groups', 
                # 'user_permissions',
            )
        }),
    )

    add_fieldsets = (
        (_("create new user"), {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2')
        }),
    )

    list_display = ('phone_number', 'is_staff', 'is_superuser', 'is_active', 'role')
    list_display_links = ('phone_number',)
    list_filter = ('is_staff', 'is_superuser', 'is_active',)
    search_fields = ('phone_number',)
    ordering = ('phone_number', 'is_staff', 'is_superuser', 'is_active', 'last_login', 'date_joined', )
    filter_horizontal = ('groups', ) #'user_permissions',)
    # list_per_page = 25

