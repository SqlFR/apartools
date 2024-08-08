from django.urls import path
from issues.views import *

app_name = 'issues'

urlpatterns = [
    path('apartment/<str:slug>/add_issue/', add_issue, name='add_issue'),
    path('delete_issue/<int:issue_id>/', delete_issue, name='delete_issue'),
]
