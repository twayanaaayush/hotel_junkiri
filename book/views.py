from django.shortcuts import HttpResponseRedirect, render, redirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied
# from django.http import HttpResponseForbidden
from django.contrib import messages
import datetime

from .forms import BookForm, AvailabilityForm
from .models import Book
from .utils import check

from index.models import Room
from user.forms import UserForm
from user.models import User
from mail.utils import send_confirm_email
from utilities.utils import url_builder_new, url_builder_addparams


def book(request):
	if request.POST:
		user_form = UserForm(request.POST)
		booking_form = BookForm(request.POST)

		if user_form.is_valid() and booking_form.is_valid():
			user_form_clean = user_form.cleaned_data
			booking_form_clean = booking_form.cleaned_data

			user = User.objects.filter(u_email = user_form_clean.get('u_email'))	#returns a queryset...so choosing the first one 
			room = Room.objects.filter(pk = booking_form_clean.get('room').pk)[0]	#returns a queryset...so choosing the first one 

			if not user.count() > 0:
				user_form.save()

			Book.objects.create(user=user[0],**booking_form_clean) #create only takes positional args..so unpacking the dict
			# booking.save()	 #create() calls save implicitely
			message = f"A {room.room_name} has been booked on the name of {user_form_clean.get('u_name')} for {booking_form_clean.get('check_in_date')}."
			messages.success(request, message+"Please Check your Mail!")

			send_confirm_email(to_email=user_form_clean.get('u_email'), message=message)

			url = url_builder_new(request.META['HTTP_REFERER'])
		else:
			messages.error(request, f"Please Enter the information correctly.")

			url = url_builder_addparams(request.META['HTTP_REFERER'], get={'error':'info-error'})

		return HttpResponseRedirect(url)
	else:
		raise PermissionDenied()
		# return HttpResponseForbidden()

def book_room_page(request, name):

	rooms = []
	room = Room.objects.get(room_name = name)
	features = room.includes.all()

	user_form = UserForm(auto_id=False)

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
				url = url_builder_new(request.META['HTTP_REFERER'])
			else:
				available =  check(request, check_in_date, check_out_date, num_guests)
				url = reverse('book_page', kwargs={'name': name})
				url = url_builder_new(url, get={'available':available, 'check_in_date':check_in_date, 'check_out_date':check_out_date, 'num': num_guests})

			return HttpResponseRedirect(url)
			# return redirect(request.META['HTTP_REFERER'])
	else:
		if 'available' in request.GET:
			available = request.GET.get('available')
			check_in_date = request.GET.get('check_in_date')
			check_out_date = request.GET.get('check_out_date')
			num_guests = request.GET.get('num')

			availability_data = {
				'check_in': check_in_date,
				'check_out': check_out_date,
				'num_guests': num_guests
			}

			booking_data = {
				'check_in_date': check_in_date,
				'check_out_date': check_out_date,
				'room': room
			}

			availability_form = AvailabilityForm(initial=availability_data, auto_id=False)
			booking_form = BookForm(initial=booking_data, auto_id=False)

			for field_name in list(booking_form.fields.keys()):
				booking_form.fields[field_name].disabled = True

			message['submitted'] = True
			message['available'] = available

			if available == "True":
				if name in request.session['available_room']:
					available_rooms = request.session['available_room']
					available_rooms.remove(name)

					message['disable'] = True
					messages.success(request, f"{name} is available from {check_in_date} to {check_out_date}.")
				else:
					message['title'] = "Other Rooms Available"
					message['body'] = f"We have the following rooms available from <span class='text-danger'>{check_in_date}</span> to <span class='text-danger'>{check_out_date}</span>."
			else:
				available_rooms = list(Room.objects.all().exclude(room_name=name))

				message['title'] = "Room Unavailable"
				if 'error' in request.session:
					message['body'] = request.session['error']
				else:
					message['body'] = f"We don't have any rooms available from <span class='text-danger'>{check_in_date}</span> to <span class='text-danger'>{check_out_date}</span>."	
			
			for room_name in available_rooms:
				rooms.append(Room.objects.get(room_name = room_name))

		else:
			rooms = list(Room.objects.all().exclude(room_name=name))

			messages.error(request, f"Please check for the availability first.")

			availability_form = AvailabilityForm(auto_id=False)
			booking_form = BookForm(auto_id=False)
			
			for field_name in list(booking_form.fields.keys()):
				booking_form.fields[field_name].disabled = True

	context = {
		'footer': 'required',
		'side_nav': 'not_required',
		'room': room,
		'rooms': rooms,
        'message': message,
		'availability_form': availability_form,
		'user_form': user_form,
		'booking_form': booking_form,
		'features': features
	}

	return render(request, 'book/book_room.html', context)