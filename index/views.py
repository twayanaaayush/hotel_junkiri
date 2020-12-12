from django.shortcuts import render, HttpResponseRedirect
# from django.urls import reverse
from .forms import AvailabilityForm

def index_page(request):
    rooms = [
        {
            'name': 'Classic Room',
            'capacity': 1,
            'price': 40.00,
            'image_url': 'classic room.jpg'
        }, 
        {
            'name': 'Double Bed Room',
            'capacity': 2,
            'price': 80.00,
            'image_url': 'double room.jpg'
        },
        {
            'name': 'Master Room',
            'capacity': 2,
            'price': 180.00,
            'image_url': 'master room.jpg'
        },
        {
            'name': 'Deluxe Suite',
            'capacity': 6,
            'price': 300.00,
            'image_url': 'deluxe suite.jpg'
        }
    ]

    services = [
        {
            'name': 'free wifi connection',
            'image_url': 'wifi.png'
        },
        {
            'name': '24 hr reception',
            'image_url': '24-hours.png'
        },
        {
            'name': 'fitness room',
            'image_url': 'barbell.png'
        },
        {
            'name': 'swimming pool',
            'image_url': 'swimming-pool.png'
        },
        {
            'name': 'room service',
            'image_url': 'service.png'
        },
        {
            'name': 'bar',
            'image_url': 'cocktail.png'
        },
    ]

    message = {
        'submitted': False,
        'available': False,
        'title': '',
        'body': ''
    }

    available = False

    if request.method == 'POST':
        availability_form = AvailabilityForm(request.POST, auto_id=False)

        if availability_form.is_valid():
            clean_data = availability_form.cleaned_data

            check_in = clean_data['check_in']
            check_out = clean_data['check_out']
            num_guests = clean_data['num_guests']

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