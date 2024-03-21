from django.shortcuts import render
from Room.models import Room
def home(request): 
    rooms = Room.objects.all()

    context = {
        'rooms': rooms,
    }
    return render (request, 'home.html',context)