from index.models import Room, RoomInstance, RoomType, Service
from django.urls import path
from django.urls import reverse, path
from django.utils.html import format_html
from django.http import HttpResponse
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
        'check_out_actions',
    )

    list_filter = ('status', 'room',)
    
    def get_urls(self):
        urls = super().get_urls()

        custom_urls = [
            path('<int:pk>/check-out/', self.check_out, name='check-out'),
        ]
        return custom_urls + urls

    def  check_out_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Check Out</a>',
            reverse('admin:check-out', args=[obj.pk]),
        )
    check_out_actions.short_description = ''

    def check_out(self, request, pk):
        return HttpResponse(f"<h1>Hello World! {pk}</h1>")

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'room_name',
        'price',
        'capacity',
    )

    list_filter = ('price',)