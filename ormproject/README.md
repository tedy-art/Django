**Django ORM**
->  ORM stands for Object Relational Mapper. 
->  The main goal of ORM is to send data between a database and models in an application. 
->  It maps a relation between the database and a model. 
->  So, ORM maps object attributes to fields of a table. 
->  The main advantage of using ORM is that it makes the entire development process fast and error-free. 
->  Essentially, it eliminates the need to write SQL code.


cmd: for open API shell
    py manage.py shell

we can do with shell
->  object read, write, where, all, update

step 1: Start virtual env

step 2: django-admin startproject ormproject

step 3: cd ormproject

step 4: python manage.py startapp ormapp

step 5: code . {for open VS code}

step 6: ormproject -> settings.py

"Add ormapp in settings.py"
e.g. "settings.py"
    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'ormapp',
    ]
step 7: ormapp-> create new folder "templates"-> create new folder as it is app name "ormapp"-> index.html 

e.g. "index.html"

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home page</title>
</head>
<body>
    <div class="container">
        <div class="jumbotron">
            <h1>This is my first ORM project</h1>
        </div>
    </div>    
</body>
</html>

step 8: ormapp-> views.py e.g. views.py

from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'templateapp\index.html')


step 9:ormproject-> urls.py e.g. "urls.py"

from django.contrib import admin
from django.urls import path
from ormapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', index_view),
]
step 10: in terminal -> run this command: ->py manage.py runserver -> http://127.0.0.1:8000