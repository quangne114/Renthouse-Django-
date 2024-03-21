from django.contrib import admin
from .models import PaymentMethods
# Register your models here.
class PaymentMethodsAdmin(admin.ModelAdmin): 
    list_display =  [field.name for field in PaymentMethods._meta.fields]
admin.site.register(PaymentMethods, PaymentMethodsAdmin),     