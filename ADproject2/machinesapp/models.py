from django.db import models
from django.forms import ModelForm
from main.models import MainUser
from hrapp.models import Employee


class Machines(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    machine=models.CharField(max_length = 200, default=None)
    machine_serial=models.CharField(max_length = 200 , default=None)
    machine_quantity=models.IntegerField(default=None)
    assigned=models.BooleanField(default=False)

class MachinesForm(ModelForm):
    class Meta :
        model = Machines
        fields = ['employee',
        'machine',
        'machine_serial',
        'machine_quantity',
        'assigned']
# Create your models here.
