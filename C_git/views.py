from django.shortcuts import render

def git(request):
    return render(request, 'git.html', {'title':'GIT'})