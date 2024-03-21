from django.db import models
from account.models import Account 
from Room.models import Room
from django.utils import timezone
from datetime import timedelta
# Create your models here.
class FeedBack(models.Model): 
    Name_PhanHoi  = models.CharField(max_length=100, unique=True) 
    slug = models.SlugField(max_length=100, unique=True)
    Description = models.TextField()
    date_feedback = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField(default=timezone.now() + timedelta(days=14))
    Room = models.ForeignKey(Room, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self): 
        return self.Name_PhanHoi