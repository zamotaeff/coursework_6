from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'role', 'id')
    list_display_links = ('email',)
    list_filter = ('role',)
    list_editable = ('role',)
    search_fields = ('first_name', 'last_name', 'email')
