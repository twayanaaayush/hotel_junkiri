from django.shortcuts import render, HttpResponseRedirect
from .helper import url_builder
from .forms import AvailabilityForm
from .models import Room, RoomInstance, Service
from user.models import Book

def index_page(request):

    rooms = list(Room.objects.all())
    services = list(Service.objects.all())

    message = {
        'submitted': False,
        'available': False,
        'title': '',
        'body': ''
    }

    if request.method == 'POST':
        availability_form = AvailabilityForm(request.POST, auto_id=False)

        if availability_form.is_valid():
            clean_data = availability_form.cleaned_data

            check_in = clean_data['check_in']
            check_out = clean_data['check_out']
            num_guests = clean_data['num_guests']

            available =  check(request, check_in, check_out, num_guests)

            url = url_builder('index', get={'available':available, 'date':check_in})
            return HttpResponseRedirect(url) 
    else:
        availability_form = AvailabilityForm(auto_id=False)

        if 'available' in request.GET:
            available = request.GET.get('available')
            date = request.GET.get('date')

            message['submitted'] = True
            message['available'] = available

            if available == "True":
                message['title'] = "Room Available"
                message['body'] = f"We have the following rooms available for <span class='text-danger'>{date}</span>."
            else:
                message['title'] = "Room Unavailable"
                if 'error' in request.session:
                    message['body'] = request.session['error']
                else:
                    message['body'] = f"We don't have any rooms available for {date}."

    context = {
        'rooms': rooms,
        'services': services,
        'availability_form': availability_form,
        'messages': message
    }

    return render(request, 'index/index.html', context)

def check(request, check_in, check_out, num_guests=1):

    filtered_room = list(Room.objects.filter(capacity__gte = num_guests))
    available_room = list()

    if len(filtered_room) > 0:
        hotel_room_count = list()
        booked_room_count = list()
        booked_room = list()

        for i in range((len(filtered_room))):
            hotel_room_count.append(RoomInstance.objects.filter(room = filtered_room[i]).count())
            booked_room_count.append(Book.objects.filter(room = filtered_room[i]).count())
            booked_room.append(list(Book.objects.filter(room = filtered_room[i])))

        for i in range(len(hotel_room_count)):
            if booked_room_count[i] < hotel_room_count[i]:
                available_room.append(filtered_room[i].room_name)
            else:
                for room in booked_room[i]:
                    if check_in > room.check_out_date or check_out < room.check_in_date:
                        available_room.append(filtered_room[i].room_name)
                    else:
                        pass
    else:
        request.session['error'] = f"No Rooms for {num_guests} guests.</br>Consider dividing the guests into different rooms."
    
    request.session['available_room'] = available_room

    return True if len(available_room) > 0 else False