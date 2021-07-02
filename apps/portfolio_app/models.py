from typing import ClassVar
from django.db import models
import datetime

# Create your models here.
class Tags(models.Model):
    title = models.CharField(max_length=15)

    def __str__(self):
        return self.title

class Status(models.Model):
    status = models.CharField(max_length=10, default='visible')

    def __str__(self):
        return self.status

class Projects(models.Model):
    img = models.ImageField(upload_to='projects', null=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    tags = models.CharField(max_length=30)
    date = models.DateField(null=True)
    url = models.CharField(max_length=20)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Visits(models.Model):
    from_to = models.CharField(max_length=50)


class Notes(models.Model):
    title = models.CharField(max_length=50)
    tags = models.CharField(max_length=200)
    date = models.DateField(default=None)
    content = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

