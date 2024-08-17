from django.urls import path

from project.views import details, apartments, add_apart

app_name = 'project'

urlpatterns = [
    path('apartments/', apartments, name='apartments'),
    path('apartments/add_apart', add_apart, name='add_apart'),
    path('apartment/<str:slug>/', details, name='details'),
]
