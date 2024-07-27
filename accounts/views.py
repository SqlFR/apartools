from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


class UserLoginView(LoginView):
    template_name = "accounts/login.html"
    next_page = reverse_lazy('index')


# def login_user(request):
#     next_url = request.GET.get('next', request.POST.get('next', 'index'))
#
#     if request.method == 'POST':
#         # Connecte l'utilisateur
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             print('User = True', next_url)
#             login(request, user)
#             return redirect('index')
#     else:
#         next_url = request.GET.get('next', '')
#         print('User = False', next_url)
#
#     return render(request, 'accounts/login.html', {'next': next_url})


def logout_user(request):
    logout(request)
    return redirect('login')
