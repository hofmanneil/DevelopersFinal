from django.db import models
from django.forms import ModelForm
from main.models import MainUser
from hrapp.models import Employee
from main.email import mail_to_helpdesk, mail_to_hr ,mail_to_employee
from django.db.models.signals import post_save
from django.dispatch import receiver


class Inventory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    machine=models.CharField(max_length=200, default=None)
    machine_serial=models.CharField(max_length=200, default=None)
    monitor_serial=models.CharField(max_length=200, default=None)
    monitor_type=models.CharField(max_length=200, default=None)
    special_request=models.BooleanField(default=False)
    special = models.CharField(max_length=200, default=None)
    keyboard = models.BooleanField(default=False)
    mouse = models.BooleanField(default=False)
    headset = models.BooleanField(default=False)
    bag= models.BooleanField(default=False)
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    fulfilled_date = models.DateTimeField(auto_now_add=True)
    thumb=models.ImageField('default.png' ,blank=True)

@receiver(post_save, sender=Employee)
def assign_hardware(sender, created, instance, **kwargs):
    if created :
        mail_to_hr(employee=instance),
        mail_to_employee(employee=instance),



class InventoryForm(ModelForm):
    class Meta :
        model = Inventory
        fields = ['employee',
        'machine',
        'machine_serial',
        'monitor_serial',
        'monitor_type',
        'special_request',
        'special',
        'keyboard',
        'mouse',
        'headset',
        'bag',
        ]
        #this shows only the 2 fields teudat_zehut and machine
        # can be modified to whatever fields are needed
