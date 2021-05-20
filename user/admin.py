from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from user.models import User

# Register your models here.
class UserAdmin(BaseUserAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active'
    )

    list_editable = ('first_name', 'last_name')

    search_fields = ('email', 'username')

    list_filter = ('created', 'modified', 'is_active')

    ordering = ('first_name', '-email')


admin.site.register(User, UserAdmin)