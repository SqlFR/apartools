from urllib.parse import urlencode

from django.shortcuts import redirect
from django.urls import reverse


# Demande à l'utilisateur de se loger avt d'atteindre l'URL
class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (not request.user.is_authenticated and
                not request.path.startswith(reverse('login')) and
                not request.path.startswith('/admin/')):
            # Redirige vers l'URL initialement renseignée
            return redirect(f"{reverse('login')}?{urlencode({'next': request.path})}")

        response = self.get_response(request)
        return response
