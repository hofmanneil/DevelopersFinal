from django.db import models
from django.forms import ModelForm
from main.models import MainUser
from hrapp.models import Employee

# Create your models here.
class Monitors(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    monitor_type=models.CharField(max_length = 200, default=None)
    monitor_serial=models.CharField(max_length = 200, default=None)
    monitor_quantity=models.IntegerField(default=None)
    assigned=models.BooleanField(default=False)

class MonitorsForm(ModelForm):
    class Meta :
        model=Monitors
        fields = ['employee',
        'monitor_type',
        'monitor_serial',
        'monitor_quantity',
        'assigned']
