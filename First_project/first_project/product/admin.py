from django.contrib import admin
from .models import laptop  #importing laptop class from models.py

# Register your models here.
admin.site.register(laptop) #registering laptop class in admin.py

class laptopAdmin(admin.ModelAdmin):
    list_display = ['password','re_password','laptop','email','about','textarea','checkbox','ram','ssd','youtube_channel']