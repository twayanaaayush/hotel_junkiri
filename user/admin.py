from django.contrib import admin
from user.models import User

from index.models import RoomInstance

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'u_name',
        'u_email',
        'u_contact',
        'u_address',
        'get_room_no',
        # 'u_room',     #if u want this, make a func that fetches this from the room_instance model
    )

    # readonly_fields = (
    #     'u_name',
    #     'u_email',
    #     'u_contact',
    #     'u_address',
    # )

    def get_room_no(self, obj):
        try:
            room = RoomInstance.objects.filter(user = obj)[0]   #above statement returns a queryset
        except (IndexError):
            room_no = None
        else:
            room_no = room.room_number
        return room_no
    
    get_room_no.short_description = 'Room Number'
    get_room_no.allow_tags = True