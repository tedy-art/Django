MVT
  |
  Template
  ->  A template consiste of static parts of the desired HTML Document as well as same special syntax describing  how dynamic content will be inserted.

steps for creating templates for websites:-

step 1: Start virtual env

step 2: django-admin startproject templateproject

step 3: cd templateproject

step 4: python manage.py startapp templateapp

step 5: code . {for open VS code}

step 6: templateproject -> settings.py

    "Add template app in settings.py"
    e.g. "settings.py"
        # Application definition

        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'templateapp',
        ]

step 7: templateapp-> create new folder "templates"-> create new folder as it is app name "templateapp"-> index.html
  e.g. "index.html"

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Templates_web</title>
    </head>
    <body>
        <h1>Welcome to world of templates..</h1>
    </body>
    </html>

step 8: templateapp-> views.py
    e.g. views.py
    
    from django.shortcuts import render

    # Create your views here.
    def index_view(request):
        return render(request, 'templateapp\index.html')

step 9:templateproject-> urls.py
    e.g. "urls.py"
    
    from django.contrib import admin
    from django.urls import path
    from templateapp.views import *

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('home/', index_view),
    ]

step 10: in terminal -> run this command:
                ->py manage.py runserver
                        -> http://127.0.0.1:8000
                        ![Html template](https://github.com/tedy-art/Django/blob/main/templateproject/templateapp/templates/templateapp/WhatsApp%20Image%202023-01-16%20at%2011.36.37%20PM.jpeg)
