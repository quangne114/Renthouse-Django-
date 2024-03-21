from django.urls import path
from . import views

urlpatterns = [
    path('RoomRentalTicket/', views.RoomRentalTicket, name='RoomRentalTicket')
]