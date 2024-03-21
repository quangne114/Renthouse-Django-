from django.db import models
from Room.models import Room
# Create your models here.
class RoomImage(models.Model):
    Name_RoomImage = models.CharField(max_length=100, unique=True)
    Room_image = models.ImageField(upload_to='photo/roomimage',null=True)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    
    def __str__(self): 
        return self.Name_RoomImage
   