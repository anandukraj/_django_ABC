from django.contrib import admin
from .models import Add
# Register your models here.

class AddAdmin(admin.ModelAdmin):
    list_display = ("Employee_name","image")
admin.site.register(Add,AddAdmin)