
from Room.models import Room
from .models import SaveRoom, SaveRoomList
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def save_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    save_room_instance, created = SaveRoom.objects.get_or_create (account =request.user)
    SaveRoomList.objects.create(room=room, saveroom=save_room_instance)
    return redirect('room_detail', category_slug=room.category.slug, room_slug=room.slug)


@login_required(login_url='login')
def saved_rooms(request):
    saved_rooms = SaveRoomList.objects.filter(saveroom__account=request.user)
    return render(request, 'rooms/saveroom_list.html', {'saved_rooms': saved_rooms})



@login_required(login_url='login')
def delete_saved_room(request, saved_room_id):
    saved_room = get_object_or_404(SaveRoomList, id=saved_room_id)

    if saved_room.saveroom.account == request.user:
        saved_room.delete()

    return redirect('saved_rooms')


