from django.shortcuts import render

# Create your views here.
def display_view(request):
    data = {1:{'name': 'Tom', 'roll':1, 'marks': 88},
        2:{'name': 'Harry', 'roll':2, 'marks': 77},
        3:{'name': 'Pavan', 'roll':3, 'marks': 66},
        4:{'name': 'Jay', 'roll':4, 'marks': 56}}
    
    context = {'data':data}
    return render(request, 'jinjaapp/display.html', context)