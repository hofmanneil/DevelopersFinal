from django.db import models
from django.forms import ModelForm
from main.models import MainUser
from main.email import mail_to_helpdesk
from django.db.models.signals import post_save
from django.dispatch import receiver

class Employee(models.Model):
    teudat_zehut=models.CharField(max_length=20, default=None)
    firstname=models.CharField(max_length=20, default=None)
    lastname=models.CharField(max_length=20, default=None)
    username=models.CharField(max_length=20, default=None)
    email_address=models.CharField(max_length=20, default=None)
    phone_number=models.CharField(max_length=20, default=None)
    department=models.CharField(max_length=20, default=None)
    office=models.CharField(max_length=20, default=None)
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    fulfilled_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname + ' ' + self.lastname

@receiver(post_save, sender=Employee)
def oncreate_user(sender, created, instance, **kwargs):
    if created :
        mail_to_helpdesk(employee=instance)






class EmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields=[
        'teudat_zehut',
        'firstname',
        'lastname',
        'phone_number',
        'department',
        'office',
]


# add later
# dropdown fields for department etc
