from datetime import date
from django.contrib import admin, messages
from django.shortcuts import HttpResponseRedirect
from index.models import Room, RoomInstance, RoomType, Service
from django.urls import reverse, path
from django.utils.html import format_html

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
            path('check-out/<int:pk>/', self.admin_site.admin_view(self.check_out_handler), name='check-out'),
        ]
        return custom_urls + urls

    def  check_out_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Check Out</a>',
            reverse('admin:check-out', args=[obj.pk]),
        )
    check_out_actions.short_description = ''

    def check_out_handler(self, request, pk):
        room_instance = RoomInstance.objects.filter(id__exact=pk).first()

        if room_instance.check_out_date > date.today():
            message = f"Check Out Date Mismatch!!"
            messages.error(request, message)
        else:    
            RoomInstance.objects.filter(id__exact=pk)\
                                .update(
                                    user=None,
                                    check_in_date=None,
                                    check_out_date=None,
                                    status = 'U',
                                )

            message = f"Check Out Successful."
            messages.success(request, message)

        # return to somewhere appropriate
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'room_name',
        'price',
        'capacity',
    )

    list_filter = ('price',)