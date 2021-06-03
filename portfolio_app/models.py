from django.db import models

# Create your models here.
class Tags(models.Model):
    title = models.CharField(max_length=15)

    def __str__(self):
        return self.title

class Projects(models.Model):
    img = models.ImageField(upload_to='projects')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)
    date = models.DateField()
    url = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Visits(models.Model):
    from_to = models.CharField(max_length=50)

