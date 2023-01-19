from django.shortcuts import render
from .models import *

# Create your views here.
def index_view(request):
    return render(request, 'ormapp/index.html')

def display_view(request):
    data = Employee.objects.all()
    context= {'data' : data}
    return render(request, 'ormapp/display.html', context)

def update_view(request, id): 
    data = Employee.objects.get(pk = id)
    context = {'data': data}
    return render(request, 'ormapp/update.html', context)