from rest_framework import serializers
from apps.portfolio_app.models import Projects

class projectsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Projects
        fields = [
            'title',
            'description',
            'tags',
            'date',
            'img',
            'url',
        ]