from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return (
            self.name
        )  # Esto hara que apareezca el nombre de la tarea en el panel de admin


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE
    )  # para relacionar ambas tablas .
    isDone = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title + " - " + self.project.name
