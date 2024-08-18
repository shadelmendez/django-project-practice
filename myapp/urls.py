from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("hello/<str:username>", views.hello),
    path("about/", views.about),
    path("projects/", views.projects),
    path("tasks", views.tasks),
    # path("create-task/<str:title><str:description><int:project>", views.create_task),
]
