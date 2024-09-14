from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy


class UserLoginView(LoginView):
    template_name = "accounts/login.html"
    next_page = reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('accounts:login')
