from datetime import date
from index.models import RoomInstance, Room
from user.models import User
from django.contrib import admin, messages
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, path
from django.utils.html import format_html
from .models import Book
from .forms import CheckInForm

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # search_fields = ("", )

    list_display = (
        'user',
        'room',
        'check_in_date',
        'check_out_date',
        'check_in_actions',
    )

    # readonly_fields = ('user',)

    list_filter = ('check_in_date', 'room',)

    def get_urls(self):
        urls = super().get_urls()

        custom_urls = [
            path('check-in/<int:pk>/', self.admin_site.admin_view(self.check_in_handler), name='check-in'),
        ]
        return custom_urls + urls

    def  check_in_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Check In</a>',
            reverse('admin:check-in', args=[obj.pk]),
        )
    check_in_actions.short_description = ''

    def check_in_handler(self, request, pk):

        booked_room_obj = Book.objects.filter(id__exact=pk).first()
        room = booked_room_obj.room
        user = booked_room_obj.user
        check_in = booked_room_obj.check_in_date
        check_out = booked_room_obj.check_out_date

        book_obj_data = {
            'room_id':room.id,
            'user':user,
            'check_in':check_in,
            'check_out':check_out
        }

        if request.POST:
            form = CheckInForm(request.POST, auto_id=False, book_obj_data=book_obj_data)

            if form.is_valid():
                form_clean = form.cleaned_data

                if not form_clean['check_in'] == date.today():
                    message = f"Check-In Date Mismatch!!"
                    messages.error(request, message)

                    # return to somewhere appropriate
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
                else:    
                    RoomInstance.objects.filter(pk = form_clean['room'].id)\
                                        .update(
                                            user=User.objects.filter(u_name__exact=form_clean['user']).first().id,
                                            check_in_date=form_clean['check_in'],
                                            check_out_date=form_clean['check_out'],
                                            status = 'O',
                                        )

                    Book.objects.filter(id__exact=pk).delete()

                    message = f"Check In Successful ({user})."
                    messages.success(request, message)

            else:
                message = f"Something went wrong, Check In Failed ({user})."
                messages.error(request, message)

            # redirect to booking page
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            # return redirect(Book)
        else:
            form = CheckInForm(book_obj_data=book_obj_data)

        context = self.admin_site.each_context(request)
        context['opts'] = self.model._meta
        context['form'] = form

        return render(request, "admin/check_in_form.html", context)