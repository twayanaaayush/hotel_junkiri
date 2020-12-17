from django.db import models
from index.models import RoomInstance, Room

class User(models.Model):
    u_name = models.CharField(max_length=50, verbose_name="Name")
    u_email = models.EmailField(verbose_name="Email")
    u_contact = models.IntegerField(verbose_name="Contact")
    u_address = models.CharField(max_length=50, verbose_name="Address")
    u_room = models.OneToOneField(RoomInstance, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.u_name


class Book(models.Model):
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.u_name}({self.room})'