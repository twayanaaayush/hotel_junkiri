from django.db import models
from django.urls import reverse

from index.models import Room
from user.models import User

class Book(models.Model):
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}({self.room})'

    # def get_absolute_url(self):
    #     return reverse('room-detail', arg=[str(self.id)])