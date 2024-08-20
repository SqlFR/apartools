from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string


from accessories.models import Accessory


def accessories_display(request, apartment):
    accessories = Accessory.objects.filter(apartment_id=apartment.id)
    return accessories


def accessory_handled(request, accessory_id):
    accessory = get_object_or_404(Accessory, id=accessory_id)
    accessory.status = 'HANDLED'
    accessory.save()

    context = {
        'accessory': accessory
    }

    return HttpResponse(render_to_string('accessories/accessory.html', context))


def accessory_delivery(request, accessory_id):
    accessory = get_object_or_404(Accessory, id=accessory_id)
    accessory.status = 'DELIVERY'
    accessory.save()

    context = {
        'accessory': accessory
    }

    return HttpResponse(render_to_string('accessories/accessory.html', context))


def accessories_to_delivery(request, apartment_id):
    accessories_handled = Accessory.objects.filter(apartment_id=apartment_id, status='HANDLED')
    accessories_to_delivery = []
    for accessory in accessories_handled:
        accessories_to_delivery.append(accessory)
    accessories_handled.update(status='DELIVERY')

    context = {
        'accessories_to_delivery': accessories_to_delivery
    }
    return render(request, 'accessories/accessory.html', context)


def accessory_not_handled(request, accessory_id):
    accessory = get_object_or_404(Accessory, id=accessory_id)
    accessory.status = 'UNAVAILABLE'
    accessory.save()

    context = {
        'accessory': accessory
    }

    return HttpResponse(render_to_string('accessories/accessory.html', context))


def accessory_to_not_handled(request, accessory_id):
    accessory = get_object_or_404(Accessory, id=accessory_id)
    accessory.status = 'NOT_HANDLED'
    accessory.save()

    context = {
        'accessory': accessory
    }

    return HttpResponse(render_to_string('accessories/accessory_not_handled.html', context))


