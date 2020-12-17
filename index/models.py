from django.db import models
from django.urls import reverse


class RoomType(models.Model):
    room_type = models.CharField(max_length=20)

    def __str__(self):
        return self.room_type


class Service(models.Model):
    service_name = models.CharField(max_length=50)
    image = models.ImageField(default='/service_images/default.png', upload_to='service_images')

    def __str__(self):
        return self.service_name


class Room(models.Model):
    room_name = models.CharField(max_length=50, help_text='Junkiri Room')
    type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(default='/room_images/default.jpg', upload_to='room_images')
    capacity = models.IntegerField(null=True, blank=True)
    price = models.IntegerField()
    includes = models.ManyToManyField(Service, help_text='services in room, eg:-wifi, tv')

    def __str__(self):
        return self.room_name

    def get_absolute_url(self):
        return reverse('room-detail', arg=[str(self.id)])


class RoomInstance(models.Model):

    class RoomStatus(models.TextChoices):
        OCCUPIED = 'O', "Occupied"
        UNOCCUPIED = 'U', "Unoccupied"
        MAINTANENCE = 'M', "Maintanence"

    room_number = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.SET_DEFAULT, default="Junkiri Room")
    status = models.CharField(max_length=1, choices=RoomStatus.choices, default=RoomStatus.MAINTANENCE)
    check_in_date = models.DateField(null=True, blank=True)
    check_out_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['check_out_date']

    def __str__(self):
        return f'{self.room_number}({self.room.room_name})'