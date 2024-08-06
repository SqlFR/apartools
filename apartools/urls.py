
from django.contrib import admin
from django.urls import path, include

from issues.views import add_issue
from project.views import index, detail
from accounts.views import logout_user, UserLoginView

urlpatterns = [
    path('', index, name='index'),
    path('login/', UserLoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', logout_user, name='logout'),
    path('admin/', admin.site.urls),
    path('apartment/<str:slug>/', detail, name='detail'),
    path('', include('issues.urls', namespace='issues'))
]
