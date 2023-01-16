
from django.contrib import admin
from django.urls import path
from jinjaapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', display_view),

]
