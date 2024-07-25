
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from main.views import index, detail
from accounts.views import login_user, logout_user

urlpatterns = [
    path('', index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', logout_user, name='logout'),
    path('admin/', admin.site.urls),
    path('apartment/<str:slug>/', detail, name='detail')
]
