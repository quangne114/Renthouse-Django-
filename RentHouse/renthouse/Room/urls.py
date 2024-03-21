
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.room, name='room'),
    path('category<slug:category_slug>/', views.room, name='Rooms_By_Category'),
    path('category<slug:category_slug>/<slug:room_slug>/', views.room_detail, name='room_detail'),
    path('search/', views.search, name='search'),
    path('add_rooms/', views.add_rooms, name='add_rooms'),
    path('rooms_list/', views.rooms_list, name='rooms_list'),
    path('room/categories/<slug:category_slug>/rooms/<slug:room_slug>/edit/', views.room_edit, name='room_edit'),
    path('room/<slug:category_slug>/<slug:room_slug>/delete/', views.room_delete, name='room_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


