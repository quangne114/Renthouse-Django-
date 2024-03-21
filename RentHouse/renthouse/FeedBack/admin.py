from django.contrib import admin
from .models import FeedBack
# Register your models here.
class FeedBackAdmin(admin.ModelAdmin): 
    list_display= [field.name for field in FeedBack._meta.fields]
admin.site.register(FeedBack, FeedBackAdmin), 