from django.contrib import admin
from django.urls import path, include

from project.views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('', include('accessories.urls', namespace='accessories')),
    path('', include('accounts.urls', namespace='accounts')),
    path('', include('issues.urls', namespace='issues')),
    path('', include('project.urls', namespace='project')),
]
