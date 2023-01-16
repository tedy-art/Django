
from django.contrib import admin
from django.urls import path
from list import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.f1),
    path('add/<int:p>/<int:q>/', views.add),
    path('sub/<int:p>/<int:q>/', views.sub),
    path('multi/<int:p>/<int:q>/', views.multi),
    path('div/<int:p>/<int:q>/', views.div),
    path('floor/<int:p>/<int:q>/', views.floor),
    path('modulo/<int:p>/<int:q>/', views.modulo),
    path('area/<int:r>/', views.area_of_circle),

]
