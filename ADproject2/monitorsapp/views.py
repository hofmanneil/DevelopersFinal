from django.shortcuts import render, redirect
from monitorsapp.models import Monitors
from main.models import MainUser
from django.contrib.auth.decorators import login_required
from monitorsapp.models import MonitorsForm


@login_required()
def monitors_page(request):
    if request.method == 'POST':
        form = MonitorsForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            #Monitors.monitor_type= request.Monitors.monitor_type
            Monitors.save(stock)
            #add flash message to confirm operation successfully completed
            return redirect('assign')

    else:
        form = MonitorsForm()
    return render(request, 'monitors.html', { 'form' : form, 'edit' : False})

@login_required()
def monitors_page_modify(request, pk):
    stock = Monitors.objects.get(pk=pk)
    if request.method == 'POST':
        form = MonitorsForm(request.POST, instance = stock)
        if form.is_valid():
            stock = form.save(commit=False)
            Monitors.monitor_type = request.monitor_type
            Monitors.save()
            #add flash message to confirm operation successfully completed
            return redirect('index')

    else:
        form = MonitorsForm(instance=inventory)
    return render(request, 'monitors.html', { 'form' : form, 'edit' : True})
