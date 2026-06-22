from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_employees', views.get_employees, name='employees'),
    path('emloyees', views.get_employees, name='get_employees'),
    path('get_jobs', views.get_jobs, name='get_jobs'),
    path('get_countries', views.get_countries, name='get_countries'),
]