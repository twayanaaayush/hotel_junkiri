from django.core.mail import message, send_mail, BadHeaderError
from django.http.response import HttpResponse

def send_confirm_email(to_email, message):

    subject = "Booking Confirmed in Hotel Junkiri"

    try:
        send_mail(
            subject=subject,
            message=message,
            from_email="hoteljunkiri1@gmail.com",
            recipient_list=[to_email],
            fail_silently=False,
        )
    except BadHeaderError:
        return HttpResponse('Invalid header found.')

def contact_mail(from_name, from_email, message):

    subject = f"Contact Mail From {from_name}"

    try:
        send_mail(
            subject=subject,
            message=f"message {from_email}",
            from_email=from_email,
            recipient_list=["hoteljunkiri1@gmail.com"],
            fail_silently=False,
        )
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
