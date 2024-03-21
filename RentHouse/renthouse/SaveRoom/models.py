from django.db import models
from Room.models import Room, Account


# Create your models here.
class SaveRoom(models.Model): 
    saveroom_id = models.CharField(max_length=250, blank=True)
    date_add = models.DateField(auto_now_add=True)
    account  = models.ForeignKey(Account, on_delete=models.CASCADE, null =True)

    def __str__(self):
        return self.saveroom_id 
    
class SaveRoomList(models.Model): 
    room = models.ForeignKey(Room, on_delete=models.CASCADE) 
    saveroom = models.ForeignKey(SaveRoom, on_delete=models.CASCADE) 

    def __str__(self):
        return self.room
