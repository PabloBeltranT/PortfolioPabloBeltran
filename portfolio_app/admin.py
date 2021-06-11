from django.contrib import admin
from django.core.exceptions import NON_FIELD_ERRORS
from .models import Projects, Tags, Status, Notes

# Register your models here.
admin.site.register(Projects)
admin.site.register(Tags)
admin.site.register(Status)
admin.site.register(Notes)