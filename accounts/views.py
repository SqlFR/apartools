from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def login_user(request):
    if request.method == 'POST':
        # Connecte l'utilisateur
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('paramètres', request.origin_url)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')

    return render(request, 'main/index.html')


def logout_user(request):
    logout(request)
    return redirect('login')
