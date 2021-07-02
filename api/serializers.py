from rest_framework import serializers
from apps.portfolio_app.models import Projects

class projectsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Projects
        fields = '__all__'


class projectsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projects

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'Nombre del proyecto': instance['title'],
            'Descripcion': instance['description'],
            'Etiquetas': instance['tags'],
            'Fecha de elaboracion': instance['date'],
            'URL del proyecto': instance['url'],
            'Path de la imagen': instance['img']
        }
        