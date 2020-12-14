from django.db import models
from django.urls import reverse
import uuid

########### table schema ############
# room = {
#     'name': 'str',
#     'type': 'room_type [1]',
#     'capacity': 'int',
#     'price': 'int',
#     'includes': 'service[1..*]' 
# }

# service = {
#     'name':'str'
# }

# room_type = {
#     'name': 'str',
# }

# room_status = {
#    'status': 'str',
# }

# room_instance = {
#     'unique_room_num': 'int<pk>',
#     'room': 'room [1]',
#     'status': 'room_status [1]',
#     'free_date': 'dateTime',
#     'user': 'user [1]'
# }

# user = {
#     'name': 'str',
#     'email': 'email',
#     'address': 'str',
#     'contact': 'int'
# }

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
        BOOKED = 'B', "Booked"
        UNRESERVED = 'R', "Unreserved"
        MAINTANENCE = 'M', "Maintanence"

    room_number = models.UUIDField(primary_key=True, default=uuid.uuid4)
    room = models.ForeignKey(Room, on_delete=models.SET_DEFAULT, default="Junkiri Room")
    status = models.CharField(max_length=1, choices=RoomStatus.choices, default=RoomStatus.MAINTANENCE)
    free_date = models.DateField()
    # user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['free_date']

    def __str__(self):
        return f'{self.id}({self.room.room_name})'