from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied
# from django.http import HttpResponseForbidden

from .forms import UserForm, BookForm
from .models import User, Book


def book(request):
	if request.POST:
		user_form = UserForm(request.POST)
		booking_form = BookForm(request.POST)

		if user_form.is_valid() and booking_form.is_valid():
			user_form_clean = user_form.cleaned_data
			booking_form_clean = booking_form.cleaned_data

			user = User.objects.filter(u_email = user_form_clean.get('u_email'))

			if not user.count() > 0:
				user_form.save()

			booking = Book.objects.create(user=user[0],**booking_form_clean) #create only takes positional args..so unpacking the dict
			# booking.save()	 #create() calls save implicitely
			
			send_email()

		else:
			pass #return some kind of error message

		return HttpResponseRedirect(reverse('index'))
	else:
		raise PermissionDenied()
		# return HttpResponseForbidden()

def send_email():
	pass