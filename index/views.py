from django.shortcuts import render, HttpResponseRedirect

from .forms import AvailabilityForm
from .models import Room, Service

from utilities.utils import url_builder
from book.forms import BookForm
from book.utils import check
from user.forms import UserForm

def index_page(request):

    rooms = list(Room.objects.all())
    services = list(Service.objects.all())

    user_form = UserForm()
    booking_form = BookForm()

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
        'user_form': user_form,
        'booking_form': booking_form,
        'messages': message
    }

    return render(request, 'index/index.html', context)

