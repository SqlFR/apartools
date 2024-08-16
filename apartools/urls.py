
from django.contrib import admin
from django.urls import path, include

from project.views import index, details, apartments_list
from accounts.views import logout_user, UserLoginView

urlpatterns = [
    path('', index, name='index'),
    path('apartments/', apartments_list, name='apartments_list'),
    path('login/', UserLoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', logout_user, name='logout'),
    path('admin/', admin.site.urls),
    path('apartment/<str:slug>/', details, name='details'),
    path('', include('issues.urls', namespace='issues')),
    path('', include('accessories.urls', namespace='accessories'))
]
