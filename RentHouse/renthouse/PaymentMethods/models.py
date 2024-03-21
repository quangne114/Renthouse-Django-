from django.db import models

# Create your models here.
class PaymentMethods(models.Model): 
    LoaiThanhToan = models.CharField(max_length=100, unique=True)
    
    def __str__(self): 
        return self.LoaiThanhToan