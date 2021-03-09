from index.models import Room, RoomInstance, RoomType, Service
from django.contrib import admin

admin.site.register(RoomType)
admin.site.register(Service)

@admin.register(RoomInstance)
class RoomInstanceAdmin(admin.ModelAdmin):
    list_display = (
        'room_number',
        'room',
        'status',
        'user',
        'check_in_date',
        'check_out_date',
    )

    list_filter = ('status', 'room',)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'room_name',
        'price',
        'capacity',
    )

    list_filter = ('price',)