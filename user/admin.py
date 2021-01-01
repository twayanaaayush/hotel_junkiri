from django.contrib import admin
from user.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'u_name',
        'u_email',
        'u_contact',
        'u_address',
        'u_room',
    )

    readonly_fields = (
        'u_name',
        'u_email',
        'u_contact',
        'u_address',
    )