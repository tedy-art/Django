
from django.contrib import admin
from django.urls import path
from templateapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', index_view),
]
