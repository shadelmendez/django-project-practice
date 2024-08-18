from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseServerError
from .models import Project, Task


# Create your views here.
def hello(request, username):
    return HttpResponse("<h1>Hello %s </h1>" % username)


def about(request):
    return render(request, "about.html")


# def index(request):
#     return HttpResponse("Este es el index")


def index(request):
    return render(request, "index.html")


# def projects(request):
#     get_projects = list(Project.objects.values())
#     return JsonResponse(get_projects, safe=False)


def projects(request):
    # title = "Django Course!!!"
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})


# def tasks(request, id):
#     task = get_object_or_404(Task, id=id)
#     print(f"task aca {task}")
#     return HttpResponse("Task' title: %s" % task.title)


def tasks(request):
    tasks = Task.objects.all()
    return render(request, "tasks.html", {"tasks": tasks})
