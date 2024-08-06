from django.urls import path
from issues.views import *

app_name = 'issues'

urlpatterns = [
    path('apartment/<str:slug>/add_issue/', add_issue, name='add_issue')
]
