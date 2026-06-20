from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Employees, Jobs, Departments, Locations, Countries, Regions, Dependents

admin.site.register(Employees)
admin.site.register(Jobs)
admin.site.register(Departments)
admin.site.register(Locations)
admin.site.register(Countries)
admin.site.register(Regions)
admin.site.register(Dependents)