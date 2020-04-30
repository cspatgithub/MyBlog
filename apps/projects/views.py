from django.shortcuts import render
from django.views import generic
from .models import Project


class ProjectListView(generic.ListView):
    model = Project
    template_name = 'projects/project_list.html'
    paginate_by = 10
