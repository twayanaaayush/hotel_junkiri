from django.core.mail import send_mail

def send_mail():
    send_mail(
        'That’s your subject',
        'That’s your message body',
        'yonko.twayana@gmail.com',
        ['aayush.twayana@gmail.com'],
        fail_silently=False,
    )