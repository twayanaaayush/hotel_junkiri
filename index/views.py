from django.shortcuts import render, HttpResponseRedirect
# from django.urls import reverse
from .forms import AvailabilityForm
from .models import Room, RoomInstance, Service

def index_page(request):

    rooms = list(Room.objects.all())
    services = list(Service.objects.all())

    message = {
        'submitted': False,
        'available': False,
        'title': '',
        'body': ''
    }

    available = True

    if request.method == 'POST':
        availability_form = AvailabilityForm(request.POST, auto_id=False)

        if availability_form.is_valid():
            clean_data = availability_form.cleaned_data

            check_in = clean_data['check_in']
            check_out = clean_data['check_out']
            num_guests = clean_data['num_guests']

            # available_rooms = list(RoomInstance.objects.filter()  )

            # return HttpResponseRedirect(reverse('index'))
            return HttpResponseRedirect(f'?available={available}&date={check_in}')

    else:
        availability_form = AvailabilityForm(auto_id=False)

        if 'available' in request.GET:
            available = request.GET.get('available')
            date = request.GET.get('date')

            message['submitted'] = True
            message['available'] = request.GET.get('available')

            if available == "True":
                message['title'] = "Room Available"
                message['body'] = f"We have the following rooms available for {date}."
            else:
                message['title'] = "Room Unavailable"
                message['body'] = f"We don't have any rooms available for {date}."

    context = {
        'rooms': rooms,
        'services': services,
        'availability_form': availability_form,
        'messages': message
    }

    return render(request, 'index/index.html', context)