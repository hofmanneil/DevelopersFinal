from django.shortcuts import render, redirect
from .models import EmployeeForm, Employee
from main.models import MainUser
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from main.email import mail_to_helpdesk


def update_csv(employee):
    print('hellow from csv update')
    print(employee.firstname)
    with open('adusers.csv','a') as file:
        file.write('{},{},{},{},{},{},{}\n'.format(employee.firstname,
employee.lastname,
employee.username,
employee.email_address,
employee.phone_number,
employee.department,
employee.office))
        print('written successfully')



def error_message(request, message):
  messages.error(request, message)
  return redirect('')

@login_required()
def employee_signup(request):
    if request.method=="POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.user = request.user
            employee.email_address= employee.firstname + '.' + employee.lastname + '@email.com'
            employee.username = employee.firstname + employee.lastname[0]
            i = 0
            while Employee.objects.filter(username=employee.username).first(): #is not None:
                employee.username = employee.username + str(i)
                i += 1

            employee.save()
            update_csv(employee)


            #add flash message to confirm operation successfully completed
            return redirect('index')
    form = EmployeeForm()
    return render(request, 'newuser.html', { 'form' : form})

@login_required()
def employee_page_modify(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance = employee)
        if form.is_valid():
            employee= form.save(commit=False)
            employee.user = request.user
            employee.save()
            #add flash message to confirm operation successfully completed
            return redirect('index')

    form = EmployeeForm(instance=employee)
    return render(request, 'newuser.html', { 'form' : form ,'edit' : True})
