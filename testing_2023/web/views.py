from django.shortcuts import render
from django.views import generic as views


# No need to test the code below
class EmployeesListView(views.ListView):
    template_name = '...'
    model = None