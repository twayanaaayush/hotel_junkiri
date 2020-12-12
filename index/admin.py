from index.models import Room, RoomInstance, RoomStatus, RoomType, Service
from django.contrib import admin

# Register your models here.
admin.site.register(RoomType)
admin.site.register(RoomStatus)
admin.site.register(Service)
admin.site.register(Room)
admin.site.register(RoomInstance)