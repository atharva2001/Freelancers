from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.contrib import messages

# Create your views here.
def home(request):
    if request.session['loggedin']:
        # print(request.session['name'])
        return render(request, 'home.html', {'uername' : request.session['name']})
    else:
        messages.error(request, "Login First!") 
        return redirect('login')

def room(request, room):
    username = request.session['name']
    # print(username)
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
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
        return redirect('home')

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']


    
    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})


