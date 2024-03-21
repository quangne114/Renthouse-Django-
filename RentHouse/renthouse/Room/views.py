from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, RoomImage
from RoomCategory.models import RoomCategory
from FeedBack.models import FeedBack
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import RoomCreateForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

def room(request, category_slug=None):
    rooms = None
    categories = None
    if category_slug is not None:
        categories = get_object_or_404(RoomCategory, slug=category_slug)
        rooms = Room.objects.filter(category=categories)
    else:
        rooms = Room.objects.all()
    
    paginator = Paginator(rooms, 6)
    page = request.GET.get('page')
    paged_rooms = paginator.get_page(page)
    
    context = {
        'rooms': paged_rooms,
    }
    return render(request, 'rooms/rooms.html', context)

def room_detail(request, category_slug, room_slug):
    try:
        single_room = Room.objects.get(category__slug=category_slug, slug=room_slug)
        images = RoomImage.objects.filter(room=single_room)
        feedback_list = FeedBack.objects.filter(Room=single_room)
    except Room.DoesNotExist:
        raise Http404("Room does not exist")
    
    context = {
        'single_room': single_room,
        'images': images,
        'feedback_list': feedback_list,
    }
    return render(request, 'rooms/room_detail.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    rooms = Room.objects.filter(Q(Address__icontains=keyword)) if keyword else Room.objects.none()
    context = {
        'rooms': rooms,
    }
    return render(request, 'rooms/rooms.html', context)

@login_required(login_url='login')
def rooms_list(request):
    rooms = Room.objects.filter(account=request.user)
    return render(request, 'rooms/rooms_list.html', {'rooms': rooms})

@login_required(login_url='login')
def add_rooms(request):
    if request.method == 'POST':
        form = RoomCreateForm(request.POST, request.FILES)
        if form.is_valid():
            room = form.save()

            for image in request.FILES.getlist('images'):
                RoomImage.objects.create(room=room, image=image)

            return redirect('home')
    else:
        form = RoomCreateForm(initial={'account': request.user})

    context = {'form': form}
    return render(request, 'rooms/add_rooms.html', context)

@login_required(login_url='login')
def room_edit(request, category_slug, room_slug):
    room = get_object_or_404(Room, category__slug=category_slug, slug=room_slug, account=request.user)

    if request.method == 'POST':
        form = RoomCreateForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            RoomImage.objects.filter(room=room).delete()
            form.save()

            for image in request.FILES.getlist('images'):
                RoomImage.objects.create(room=room, image=image)

            return redirect('room_detail', category_slug=room.category.slug, room_slug=room_slug)
    else:
        form = RoomCreateForm(instance=room)

    context = {'form': form, 'room': room}
    return render(request, 'rooms/room_edit.html', context)

@login_required(login_url='login')
def room_delete(request, category_slug, room_slug):
    room = get_object_or_404(Room, category__slug=category_slug, slug=room_slug, account=request.user)
    if request.method == 'POST':
        room.delete()
        return redirect('rooms_list')
    
    return render(request, 'rooms/room_confirm_delete.html', {'room': room})