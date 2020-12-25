from django.core.mail import message, send_mail, BadHeaderError
from django.http.response import HttpResponse

def send_confirm_email(to_email, message):

    subject = "Booking Confirmed in Hotel Junkiri"

    try:
        send_mail(
            subject=subject,
            message=message,
            from_email="hotel.junkiri@gmail.com",
            recipient_list=[to_email],
            fail_silently=False,
        )
    except BadHeaderError:
        return HttpResponse('Invalid header found.')