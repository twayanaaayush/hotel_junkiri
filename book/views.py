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
from utilities.utils import url_builder_new


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
		else:
			messages.error(request, f"Please Enter the information correctly.")

		return HttpResponseRedirect(reverse('index'))
	else:
		raise PermissionDenied()
		# return HttpResponseForbidden()

def book_room_page(request, name):

	room = Room.objects.get(room_name = name)
	features = room.includes.all()

	user_form = UserForm()
	booking_form = BookForm()

	check_in_date=''
	check_out_date=''

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

			check_in_date = clean_data['check_in']
			check_out_date = clean_data['check_out']
			num_guests = clean_data['num_guests']

			if datetime.date.today() >= check_in_date:
				messages.error(request, 'Please select a date in the future.')
				url = url_builder_new(request.META['HTTP_REFERER'])
			else:
				available =  check(request, check_in_date, check_out_date, num_guests)
				url = url_builder_new(request.META['HTTP_REFERER'], get={'available':available, 'check-in-date':check_in_date, 'check-out-date':check_out_date})

			return HttpResponseRedirect(url)
			# return redirect(request.META['HTTP_REFERER'])
	else:
		if 'available' in request.GET:
			available = request.GET.get('available')
			check_in_date = request.GET.get('check-in-date')
			check_out_date = request.GET.get('check-out-date')
			num_guests = request.GET.get('num')

			data = {
				'check_in': check_in_date,
				'check_out': check_out_date,
				'num_guests': num_guests
			}
			availability_form = AvailabilityForm(initial=data, auto_id=False)

			message['submitted'] = True
			message['available'] = available

			if available == "True":
				message['title'] = "Room Available"
				message['body'] = f"We have the following rooms available from <span class='text-danger'>{check_in_date}</span> to <span class='text-danger'>{check_out_date}</span>."
			else:
				message['title'] = "Room Unavailable"
				if 'error' in request.session:
					message['body'] = request.session['error']
				else:
					message['body'] = f"We don't have any rooms available from <span class='text-danger'>{check_in_date}</span> to <span class='text-danger'>{check_out_date}</span>."

		else:
			availability_form = AvailabilityForm(auto_id=False)
	
	context = {
		'footer': 'required',
		'side_nav': 'not_required',
		'room': room,
        'message': message,
		'check_in_date': check_in_date,
		'check_out_date': check_out_date,
		'availability_form': availability_form,
		'user_form': user_form,
		'booking_form': booking_form,
		'features': features
	}

	return render(request, 'book/book_room.html', context)