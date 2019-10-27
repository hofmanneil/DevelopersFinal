from django.contrib import admin
from . models import Inventory
from . models import Employee

# Register your models here.
admin.site.register(Inventory)
admin.site.register(Employee)
