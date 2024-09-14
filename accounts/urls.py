from django.urls import path
from accounts.views import logout_user, UserLoginView

app_name = 'accounts'

urlpatterns = [
    path('login/', UserLoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', logout_user, name='logout'),
]
