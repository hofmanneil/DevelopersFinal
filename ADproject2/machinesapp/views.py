from django.shortcuts import render, redirect
from machinesapp.models import Machines
from main.models import MainUser
from django.contrib.auth.decorators import login_required
from machinesapp.models import MachinesForm



@login_required()
def machine_page(request):
    if request.method == 'POST':
        form = MachinesForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            # Machines.machine = request.machine
            form.save(stock)
            #add flash message to confirm operation successfully completed
            return redirect('assign')

    else:
        form = MachinesForm()
    return render(request, 'machines.html', { 'form' : form, 'edit' : False})

@login_required()
def machine_page_modify(request, pk):
    machines = Machines.objects.get(pk=pk)
    if request.method == 'POST':
        form = MachinesForm(request.POST, instance = 'machines')
        if form.is_valid():
            machines = form.save(commit=False)
            machines.user = request.user
            machines.save()
            #add flash message to confirm operation successfully completed
            return redirect('index')

    else:
        form = MachinesForm(instance=inventory)
    return render(request, 'machines.html', { 'form' : form, 'edit' : True})



# @login_required()
# def inventory_page_modify(request, pk):
#     inventory = Inventory.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = InventoryForm(request.POST, instance = inventory)
#         if form.is_valid():
#             inventory = form.save(commit=False)
#             inventory.user = request.user
#             inventory.save()
#             #add flash message to confirm operation successfully completed
#             return redirect('index')
#
#     else:
#         form = InventoryForm(instance=inventory)
#     return render(request, 'inventory.html', { 'form' : form, 'edit' : True})
# # Create your views here.

# Create your views here.
