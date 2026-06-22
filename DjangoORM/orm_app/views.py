from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Employees, Jobs, Countries
def home(request):
        return HttpResponse("Semple data.  "
                            "<a href='/get_employees'>   employees</a>,"
                            "<a href='/get_jobs'>   Jobs</a>,"
                            "<a href='/get_countries'>  Countries</a>")


def get_employees(request):
    # employees = Employees.objects.filter(first_name="Lex")
    # employees = Employees.objects.filter(last_name="Khoo")
    employees = Employees.objects.all()
    employees_list = ""
    for employee in employees:
        employees_list += f"<li>{employee.first_name} {employee.last_name}</li>"
    return HttpResponse(employees_list)

def get_jobs(request):
    # jobs = Jobs.objects.filter(job_id=1)
    # jobs = Jobs.objects.filter(min_salary=2500.0)
    jobs = Jobs.objects.filter(max_salary=30000.0)
    jobs_list = ""
    for job in jobs:
        jobs_list += f"<li>{job.job_title}</li>"
    return HttpResponse(jobs_list)

def get_countries(request):
    # countries = Countries.objects.filter(country_name="United Kingdom")
    countries = Countries.objects.filter(country_id="UK")
    # countries = Countries.objects.filter(
    #     country_id="BE",
    #     country_name="Belgium"
    # )
    countries_list = ""
    for country in countries:
        countries_list += f"""* {country.country_name}"""
    return HttpResponse(countries_list)