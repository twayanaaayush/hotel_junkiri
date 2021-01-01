from django.contrib import admin
from django.db import models
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'room',
        'check_in_date',
        'check_out_date',
    )

    readonly_fields = ('user',)

    list_filter = ('check_in_date', 'room',)