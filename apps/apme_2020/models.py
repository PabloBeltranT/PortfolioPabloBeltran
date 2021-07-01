from django.db import models

# Create your models here.
class Login(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, null=True)

class defaultNames(models.Model):
    module_01 = models.CharField(default='Module #01', max_length=30)
    module_02 = models.CharField(default='Module #02', max_length=30)
    module_03 = models.CharField(default='Module #03', max_length=30)
    module_04 = models.CharField(default='Module #04', max_length=30)
    module_05 = models.CharField(default='Module #05', max_length=30)
    module_06 = models.CharField(default='Module #06', max_length=30)
    module_07 = models.CharField(default='Module #07', max_length=30)
    module_08 = models.CharField(default='Module #08', max_length=30)
    module_09 = models.CharField(default='Module #09', max_length=30)
    module_10 = models.CharField(default='Module #10', max_length=30)
    module_11 = models.CharField(default='Module #11', max_length=30)
    module_12 = models.CharField(default='Module #12', max_length=30)
    module_13 = models.CharField(default='Module #13', max_length=30)
    module_14 = models.CharField(default='Module #14', max_length=30)
    module_15 = models.CharField(default='Module #15', max_length=30)
    module_16 = models.CharField(default='Module #16', max_length=30)
    module_07 = models.CharField(default='Module #17', max_length=30)
    module_18 = models.CharField(default='Module #18', max_length=30)
    module_19 = models.CharField(default='Module #19', max_length=30)
    module_20 = models.CharField(default='Module #20', max_length=30)