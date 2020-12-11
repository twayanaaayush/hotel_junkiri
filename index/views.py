from django.shortcuts import render
# from django.http import HttpResponse

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

    context = {
        'rooms': rooms,
        'services': services
    }

    return render(request, 'index/index.html', context)
    # return HttpResponse('<h1>Hello World!</h1>')