from index.models import Room, RoomInstance
from book.models import Book

# also check for bookings done through admin panel

def check(request, check_in, check_out, num_guests=1):

    filtered_room = list(Room.objects.filter(capacity__gte = num_guests))
    available_room = list()

    if len(filtered_room) > 0:
        hotel_room_count = list()
        booked_room_count = list()
        booked_room = list()

        for i in range((len(filtered_room))):
            hotel_room_count.append(RoomInstance.objects.filter(room = filtered_room[i]).count())
            booked_room_count.append(Book.objects.filter(room = filtered_room[i]).count())
            booked_room.append(list(Book.objects.filter(room = filtered_room[i])))

        for i in range(len(hotel_room_count)):
            if booked_room_count[i] < hotel_room_count[i]:
                available_room.append(filtered_room[i].room_name)
            else:
                for room in booked_room[i]:
                    if check_in > room.check_out_date or check_out < room.check_in_date:
                        available_room.append(filtered_room[i].room_name)
                    else:
                        pass
    else:
        request.session['error'] = f"No Rooms for {num_guests} guests.</br>Consider dividing the guests into different rooms."
    
    request.session.modified = True
    request.session['available_room'] = available_room  #only contains the name of the room
    print(request.session['available_room'])

    return True if len(available_room) > 0 else False