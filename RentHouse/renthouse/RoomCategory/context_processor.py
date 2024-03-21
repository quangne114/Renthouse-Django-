from .models import RoomCategory

def menu_links(request):
    links = RoomCategory.objects.all()
    return dict(links=links)