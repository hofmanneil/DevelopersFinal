from django.shortcuts import render,redirect
from . models import Inventory, InventoryForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from main.email import mail_to_hr, mail_to_employee


@login_required()
def inventory_page(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            inventory = form.save(commit=False)
            inventory.user = request.user
            inventory.save()
            #add flash message to confirm operation successfully completed
            return redirect('index')

    else:
        form = InventoryForm()
    return render(request, 'inventory.html', { 'form' : form, 'edit' : False})

@login_required()
def inventory_page_modify(request, pk):
    inventory = Inventory.objects.get(pk=pk)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance = inventory)
        if form.is_valid():
            inventory = form.save(commit=False)
            inventory.user = request.user
            inventory.save()
            #add flash message to confirm operation successfully completed
            return redirect('index')

    else:
        form = InventoryForm(instance=inventory)
    return render(request, 'inventory.html', { 'form' : form, 'edit' : True})
# Create your views here.
