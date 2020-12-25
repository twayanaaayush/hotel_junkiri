from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied
# from django.http import HttpResponseForbidden
from django.contrib import messages

from .forms import BookForm
from .models import Book

from index.models import Room
from user.forms import UserForm
from user.models import User
from mail.utils import send_mail

def book(request):
	if request.POST:
		user_form = UserForm(request.POST)
		booking_form = BookForm(request.POST)

		if user_form.is_valid() and booking_form.is_valid():
			user_form_clean = user_form.cleaned_data
			booking_form_clean = booking_form.cleaned_data

			user = User.objects.filter(u_email = user_form_clean.get('u_email'))
			room = Room.objects.filter(pk = booking_form_clean.get('room').pk)[0]	#returns a queryset...so choosing the first one 

			if not user.count() > 0:
				user_form.save()

			Book.objects.create(user=user[0],**booking_form_clean) #create only takes positional args..so unpacking the dict
			# booking.save()	 #create() calls save implicitely
			messages.success(request, f"A {room.room_name} has been booked on the name of {user_form_clean.get('u_name')} for {booking_form_clean.get('check_in_date')}. Please Check your Mail!")

			send_mail()
		else:
			messages.error(request, f"Please Enter the information correctly.")

		return HttpResponseRedirect(reverse('index'))
	else:
		raise PermissionDenied()
		# return HttpResponseForbidden()