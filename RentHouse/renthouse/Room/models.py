from django.db import models
from RoomCategory.models import RoomCategory
from account.models import Account
from django.utils import timezone
from datetime import timedelta
from RoomArea.models import RoomArea
from django.urls import reverse

# Create your models here.
class Room(models.Model):
    Name_Room = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    Address = models.CharField(max_length=250, unique=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Price_deposit = models.DecimalField(max_digits=10, decimal_places=2)
    Description = models.TextField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)
    mainimage = models.ImageField(upload_to='photo/mainimage', blank=True, null=True)
    roomarea = models.ForeignKey(RoomArea, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField(default=timezone.now() + timedelta(days=14))

    def get_url(self):
        return reverse('room_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.Name_Room

class RoomImage(models.Model):
    room = models.ForeignKey(Room, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='room_images/')

    def __str__(self):
        return self.room.Name_Room
    
