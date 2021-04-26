from django.db import models

class Sesion(models.Model):
    user=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.user
    
