**"Static files in Django"**
->  css, js, images, videos..or more

->  Websites generally need to serve additional files such as images,   JavaScript, or CSS. In Django, we refer to these files as “static files”. Django provides django.contrib.staticfiles to help you manage them.

    *Folder creation :- *
        static(folder)
            -> css(folder)
            -> js(folder)
            -> Images(folder)
            -> Videos(folder)

    Syntax :-
        {%   %}  ->CODE BLOCK

**Where we can write code blocks**
inside html file
    -> 
        <!DOCTYPE html>
        <html lang="en">
        <head>
            {% load static %}
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="{% static 'css/style.css' %}">
            <title>Static app</title>
        </head>
        <body>
            <div>
                <h1>Wakanda forever</h1>
            </div>
        </body>
        </html>

steps for creating static fileand folders for websites:-

step 1: Start virtual env

step 2: django-admin startproject staticproject

step 3: cd staticproject

step 4: python manage.py startapp staticapp

step 5: code . {for open VS code}

step 6: staticproject -> settings.py

    "Add app in settings.py"
    e.g. "settings.py"
        # Application definition

        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'staticapp',
        ]

step 7: staticapp-> templates-> staticapp-> index.html
    e.g.
    <!DOCTYPE html>
    <html lang="en">
    <head>
        {% load static %}
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="{% static 'css/style.css' %}">
        <title>Static app</title>
    </head>
    <body>
        <div>
            <h1>Wakanda forever</h1>
        </div>
    </body>
    </html>
    
step 8: staticapp
            ->static(create folder)
                    -> css(create folder)
                    -> js(create folder)
                    -> Images(create folder)
                    -> Videos(create folder)

step 9: add css in static folder
        style.css
            body{
                background-image: url("https://i.stack.imgur.com/jGlzr.png");
                background-color: blue;
            }

            .container{
                height: 200px;
                background-color: #cccccc;
                background-image: radial-gradient(red, yellow);
            }
step 10: staticapp-> viwes.py
    from django.shortcuts import render

    # Create your views here.
    def index_views(request):
        
        return render(request, 'staticapp/index.html')

step 11: staticproject-> urls.py
        urls.py
        e.g.
        from django.contrib import admin
        from django.urls import path
        from staticapp.views import *

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('home/', index_views),

        ]

step 12: new terminal
            ->python manage.py runserver
                    -> http://127.0.0.1:8000/
                    ![screenshot](https://github.com/tedy-art/Django/blob/main/staticproject/staticapp/static/images/screenshot.jpeg)