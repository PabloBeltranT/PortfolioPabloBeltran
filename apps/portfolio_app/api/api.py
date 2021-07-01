from apps.portfolio_app.models import Projects, Visits
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import projectsSerializer

@api_view(['GET', 'POST'])
def portfolio_api(request):

    if request.method == 'GET':
        projects = Projects.objects.all()
        projects_serializer = projectsSerializer(projects, many=True)
        data = {
            'title':'project1'
        }
        return Response(data=projects_serializer.data, status=status.HTTP_200_OK)    


    elif request.method == 'POST':
        pass


@api_view(['GET', 'PUT', 'DELETE'])
def portfolio_api_detail(request, id):

    if request.method == 'GET':
        pass


    elif request.method == 'PUT':
        pass


    elif request.method == 'DELETE':
        pass