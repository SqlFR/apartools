from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django_ratelimit.decorators import ratelimit

from accessories.models import Apartment, Accessory


# Vue pour la gestion des accessoires


