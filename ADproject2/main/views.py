from django.shortcuts import render, redirect
from hrapp.models import EmployeeForm ,Employee
from main.models import MainUser
from helpdesk.models import InventoryForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.db.models import Q


# Create your views here.


def index(request):
    return render (request,'index.html')


@login_required()
def split_users(request):
    hrgroup=Group.objects.get(name='HR user')
    helpdeskgroup=Group.objects.get(name='Helpdesk')
    if hrgroup in request.user.groups.all():
        return redirect('create' )
    elif helpdeskgroup in request.user.groups.all():
        return redirect('assign')
    else :
        return redirect('index')

@login_required()
def search(request):
    if request.method=='POST':
        querytext=request.POST.get('search',' ')
        employees=Employee.objects.filter(
        Q(firstname__icontains=querytext) |
        Q(teudat_zehut=querytext)
        )
        return render(request,'search.html', {'employees' : employees})
    return render(request,'search.html')
