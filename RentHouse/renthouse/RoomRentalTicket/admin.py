from django.contrib import admin
from .models import RoomRentalTicket
# Register your models here.
class RoomRentalTicketAdmin(admin.ModelAdmin): 
    list_display = [field.name for field in RoomRentalTicket._meta.fields]
admin.site.register(RoomRentalTicket, RoomRentalTicketAdmin), 