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


class RoomStatus(models.Model):
    status = models.CharField(max_length=20, default="Maintenance")

    def __str__(self):
        return self.status


class Service(models.Model):
    service_name = models.CharField(max_length=50)

    def __str__(self):
        return self.service_name


class Room(models.Model):
    room_name = models.CharField(max_length=50, default="Junkiri Room")
    type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    image_url = models.CharField(max_length=200, blank=True, null=True)
    capacity = models.IntegerField(null=True, blank=True)
    price = models.IntegerField()
    includes = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, help_text='services in room, eg:-wifi, tv')

    def __str__(self):
        return self.room_name

    def get_absolute_url(self):
        return reverse('room-detail', arg=[str(self.id)])


class RoomInstance(models.Model):
    room_number = models.UUIDField(primary_key=True, default=uuid.uuid4)
    room = models.ForeignKey(Room, on_delete=models.SET_DEFAULT, default="Junkiri Room")
    status = models.ForeignKey(RoomStatus, on_delete=models.SET_DEFAULT, default="Maintenance")
    free_date = models.DateField()
    # user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['free_date']

    def __str__(self):
        return f'{self.id}({self.room.room_name})'