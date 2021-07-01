from django.urls import path, include
from .views import index, desktop_gui, notes

urls_views = [
    path('', index),
    path('desktop_gui/', desktop_gui),
    path('notes/', notes),
]

urls_api = [
    path('portfolio/', include('apps.portfolio_app.api.routers')),
]

urlpatterns = urls_views + urls_api