from collections import namedtuple
from django import urls
from django.contrib import admin
from django.http.response import Http404, HttpResponse
from django.urls import reverse, path
from django.utils.html import format_html
from django.db import models
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # search_fields = ("", )

    list_display = (
        'user',
        'room',
        'check_in_date',
        'check_out_date',
        'book_actions',
    )

    # readonly_fields = ('user',)

    list_filter = ('check_in_date', 'room',)

    def get_urls(self):
        urls = super().get_urls()

        custom_urls = [
            path('<int:pk>/check-in/', self.check_in, name='check-in'),
        ]
        return custom_urls + urls

    def  book_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Check In</a>',
            reverse('admin:check-in', args=[obj.pk]),
        )
    book_actions.short_description = ''
    book_actions.allow_tags = True

    def check_in(self, request, pk):
        return HttpResponse(f"<h1>Hello World! {pk}</h1>")