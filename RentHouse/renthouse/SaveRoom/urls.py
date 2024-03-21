from django.urls import path 
from . import views
urlpatterns = [
    path('save_room/<int:room_id>/', views.save_room, name='save_room'),
    path('saved_rooms/', views.saved_rooms, name='saved_rooms'),
    path('delete-saved-room/<int:saved_room_id>/', views.delete_saved_room, name='delete_saved_room'),
]
