from django.contrib import admin
from .models import Projects, Tags, Status

# Register your models here.
admin.site.register(Projects)
admin.site.register(Tags)
admin.site.register(Status)