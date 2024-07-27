
from django.contrib import admin
from django.urls import path

from main.views import index, detail
from accounts.views import logout_user, UserLoginView

urlpatterns = [
    path('', index, name='index'),
    path('login/', UserLoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', logout_user, name='logout'),
    path('admin/', admin.site.urls),
    path('apartment/<str:slug>/', detail, name='detail')
]
