from django.contrib import admin
from .models import RoomCategory
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('Name_LoaiPhong',)}
    list_display = ('Name_LoaiPhong','slug')
admin.site.register(RoomCategory,CategoryAdmin)