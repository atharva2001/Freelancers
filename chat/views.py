from django.shortcuts import render, redirect
from chat.models import Room, Message, RoomMore
from django.http import HttpResponse, JsonResponse
from django.contrib import messages

# Create your views here.
def home(request):
    if request.session['loggedin']:
        return render(request, 'chat/home.html', {'uername' : request.session['name']})
    else:
        messages.error(request, "Login First!") 
        return redirect('login')

def room(request, room):
    username = request.session['name']
    room_details = Room.objects.get(name=room)
    room_more = RoomMore.objects.get(name=room)
    # print(username)

    val = str(room_more.start_time).split(":")
    start_hrs = int(val[0])
    start_min = int(val[1])
    start_sec = int(val[2])

    val = str(room_more.start_date).split("-")
    start_year = int(val[0])
    start_month = int(val[1])
    start_day = int(val[2])

    val = str(room_more.end_time).split(":")
    end_hrs = int(val[0])
    end_min = int(val[1])
    end_sec = int(val[2])

    val = str(room_more.end_date).split("-")
    end_year = int(val[0])
    end_month = int(val[1])
    end_day = int(val[2])

    # print(val)

    request.session["hashmap"] = [room, start_hrs, start_min, start_sec, end_hrs, end_min, end_sec]

    return render(request, 'chat/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details,
        'start_hrs' : start_hrs,
        'start_min' : start_min,
        'start_sec' : start_sec,
        'end_hrs' : end_hrs,
        'end_min' : end_min,
        'end_sec' : end_sec,
        'start_year' : start_year,
        'start_month' : start_month,
        'start_day' : start_day,
        'end_year' : end_year,
        'end_month' : end_month,
        'end_day' : end_day
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.session['name']
    request.session['username'] = username
    # print(username)
    if Room.objects.filter(name=room).exists():
        return redirect('/chat/'+room)
    else:
        # new_room = Room.objects.create(name=room)
        # new_room.save()
        messages.error(request, 'Room doesnt exists!!')
        return redirect('chat/home')

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    # print(request.session["hashmap"])
    change = RoomMore.objects.get(id=room_id)
    if int(change.winner_amount) > int(message):
        change.winner_amount = message
        change.winner_name = username
        change.save()

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    more = RoomMore.objects.get(name=room)
    info = [more.winner_amount, more.winner_name]
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values()), "info" : info})


