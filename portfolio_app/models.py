from django.db import models

# Create your models here.
class Visits(models.Model):
    from_to = models.CharField(max_length=50)