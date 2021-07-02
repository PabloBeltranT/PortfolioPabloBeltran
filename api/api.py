from apps.portfolio_app.models import Projects, Visits
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import projectsSerializer, projectsListSerializer

@api_view(['GET', 'POST'])
def portfolio_api(request):

    if request.method == 'GET':

        projects = Projects.objects.all().values('id','title', 'description', 'tags', 'date', 'img', 'url')
        projects_serializer = projectsListSerializer(projects, many=True)

        return Response(data=projects_serializer.data, status=status.HTTP_200_OK)    
 

    elif request.method == 'POST':

        new_project = projectsSerializer(data=request.data)
        if new_project.is_valid():
            new_project.save()
            return Response(data=new_project.data)
        return Response(data=new_project.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def portfolio_api_detail(request, id):

    try:
        project_solicited = Projects.objects.filter(id=id).first()
    except:
        return Response(data='Object No Find!', status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'GET':
        project_find = projectsSerializer(project_solicited)
        return Response(data=project_find.data, status=status.HTTP_200_OK)


    elif request.method == 'PUT':

        update_project = projectsSerializer(project_solicited, data=request.data)

        if update_project.is_valid():
            update_project.save()
            return Response(data=update_project.data, status=status.HTTP_202_ACCEPTED)

        return Response(data=update_project.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':

        project_solicited.delete()
        return Response(status=status.HTTP_200_OK)