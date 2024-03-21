from django.contrib import admin 
from .models import Room
# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_display = ['Name_Room', 'Price','Address','Price','Price_deposit','category','created_date','expiration_date']
    prepopulated_fields = {'slug':('Name_Room',)}
admin.site.register(Room, RoomAdmin), 
