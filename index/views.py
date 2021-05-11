from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
import datetime

from .models import Room, Service
from .forms import ContactForm

from utilities.utils import url_builder
from book.forms import BookForm, AvailabilityForm
from book.utils import check
from user.forms import UserForm
from mail.utils import contact_mail

def index_page(request):

    rooms = list(Room.objects.all())
    services = list(Service.objects.all())

    check_in_date=''
    check_out_date=''
    num_guests = ''

    message = {
        'submitted': False,
        'available': False,
        'disable': False,
        'title': '',
        'body': ''
    }

    if request.method == 'POST':
        availability_form = AvailabilityForm(request.POST, auto_id=False)

        if availability_form.is_valid():
            clean_data = availability_form.cleaned_data

            check_in_date = clean_data['check_in']
            check_out_date = clean_data['check_out']
            num_guests = clean_data['num_guests']

            if datetime.date.today() >= check_in_date:
                messages.error(request, 'Please select a date in the future.')
                url = url_builder('index')
            else:
                available =  check(request, check_in_date, check_out_date, num_guests)
                url = url_builder('index', get={'available':available, 'check_in_date':check_in_date, 'check_out_date':check_out_date, 'num':num_guests})

            return HttpResponseRedirect(url) 
    else:
        availability_form = AvailabilityForm(auto_id=False)

        if 'available' in request.GET:
            available = request.GET.get('available')
            check_in_date = request.GET.get('check_in_date')
            check_out_date = request.GET.get('check_out_date')
            # num_guests = request.GET.get('num')

            message['submitted'] = True
            message['available'] = available

            if available == "True":
                message['title'] = "Room Available"
                message['body'] = f"We have the following rooms available from <span class='text-danger'>{check_in_date}</span> to <span class='text-danger'>{check_out_date}</span>."
            else:
                message['title'] = "Room Unavailable"
                if 'error' in request.session:
                    message['body'] = request.session['error']

                    del request.session['error']
                else:
                    message['body'] = f"We don't have any rooms available from <span class='text-danger'>{check_in_date}</span> to <span class='text-danger'>{check_out_date}</span>."

    context = {
        'rooms': rooms,
        'services': services,
        'availability_form': availability_form,
        # 'check_in_date': check_in_date,
        # 'check_out_date': check_out_date,
        # 'num_guests': num_guests,
        'message': message,
        'footer': 'required',
        'side_nav': 'required'
    }

    return render(request, 'index/index.html', context)

def about_page(request):
    context = {
        'footer': 'required',
        'side_nav': 'required'
    }
    return render(request, 'index/about.html', context)

def contact_page(request):

    if request.method == 'POST':
        contact_form = ContactForm(request.POST, auto_id=False)

        if contact_form.is_valid():
            clean_data = contact_form.cleaned_data
            contact_mail(clean_data['name'], clean_data['email'], clean_data['message'])
            return HttpResponseRedirect(reverse('contact'))
    else:
        contact_form = ContactForm(auto_id=False)

    context = {
        'contact_form': contact_form,
    }
    return render(request, 'index/contact.html', context)

def bar_page(request):
    context = {
        'footer': 'required',
        'side_nav': 'required'
    }
    return render(request, 'index/bar.html', context)

def restaurant_page(request):
    context = {
        'footer': 'required',
        'side_nav': 'required'
    }
    return render(request, 'index/restaurant.html', context)

def room_page(request, pk):

    rooms = list(Room.objects.all().exclude(id=pk))
    room = Room.objects.get(pk = pk)
    features = room.includes.all()

    context = {
        'footer': 'required',
        'side_nav': 'not_required',
        'room': room,
        'rooms':rooms,
        'features': features
    }
    return render(request, 'index/room.html', context)
    