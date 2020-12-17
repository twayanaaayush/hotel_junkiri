from django.contrib import admin
from user.models import Book, User

admin.site.register(User)
admin.site.register(Book)