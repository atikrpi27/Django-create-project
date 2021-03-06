from django.shortcuts import render
from django.http import HttpResponse
from . forms import MenuForm
from django.contrib import messages

from website_template.models import Menu

# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def menu(request):    
    if request.method == 'POST':
        form = MenuForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,('Food is added Successfully!'))
    food = Menu.objects.all
    dic = {'text1':'Our Food Details ' , 'food_list': food , 'pr':'$'}
    return render(request,'menu.html', dic)

def reservation(request):
    return render(request,'reservation.html')

def team(request):
    return render(request,'team.html')

def special_dishes(request):
    return render(request,'special-dishes.html')

def base(request):
    return render(request,'base.html')