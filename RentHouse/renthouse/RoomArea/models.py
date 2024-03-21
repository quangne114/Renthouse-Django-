from django.db import models

# Create your models here.
class RoomArea(models.Model): 
    Area = models.IntegerField()
    Unit = models.CharField(max_length=50)

    def __str__(self): 
        return f"{self.Area} {self.Unit}"