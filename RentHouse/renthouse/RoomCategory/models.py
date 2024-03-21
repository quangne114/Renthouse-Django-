from django.db import models
from django.urls import reverse
# Create your models here.
class RoomCategory(models.Model): 
    Name_LoaiPhong = models.CharField(max_length=200, unique=True)
    Url_LoaiPhong = models.ImageField(upload_to='photo/categories', blank=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    class Meta: 
        verbose_name = 'Room Category'
        verbose_name_plural = 'Room Categories'
    
    def get_url(self):
        return reverse('Rooms_By_Category', args = [self.slug])
    
    
    def __str__(self):
        return self.Name_LoaiPhong