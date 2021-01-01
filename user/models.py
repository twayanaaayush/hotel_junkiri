from django.db import models

from index.models import RoomInstance

class User(models.Model):
    u_name = models.CharField(max_length=50, verbose_name="Name")
    u_email = models.EmailField(verbose_name="Email")
    u_contact = models.IntegerField(verbose_name="Contact")
    u_address = models.CharField(max_length=50, verbose_name="Address")
    u_room = models.OneToOneField(RoomInstance, on_delete=models.SET_NULL, null=True) #get data from bookings and only show room_instance by filtering from room

    def __str__(self):
        return self.u_name