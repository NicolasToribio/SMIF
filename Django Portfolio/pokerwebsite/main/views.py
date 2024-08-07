from django.shortcuts import render, get_object_or_404
from .models import Project,Tag


def home(request):
    projects = Project.objects.all() #gives us access to all of the different projects we have just created
    tags = Tag.objects.all()
    return render(request, "home.html", {"projects": projects, "tags": tags}) #renders the home.html file whenever we return home - we pass it a dictionary that contains key-value pairs that we can pass into the template and use to render different dynamic data 


def contact(request):
    return render(request, "contact.html")


def project(request, id):
    project = get_object_or_404(Project, pk=id) #helper function in django that looks for a project with the primary key id - if found will be rendered, if not returns a 404
    return render(request, "project.html",{"project": project}) #We pass this to the template so we have a project variable that contains the project information















# Create your views here. View is a function that is called when we go to a specific root/directory.