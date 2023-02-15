from django.shortcuts import render
from django.views import generic as views

from testing_2023.web.models import Profile


# No need to test the code below
class EmployeesListView(views.ListView):
    template_name = 'profile/list.html'
    model = Profile