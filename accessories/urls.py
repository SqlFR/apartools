from django.urls import path
from accessories.views import *

app_name = 'accessories'

urlpatterns = [
    path('accessory/handled/<int:accessory_id>', accessory_handled, name='accessory_handled'),
    path('accessory/delivery/<int:accessory_id>', accessory_delivery, name='accessory_delivery'),
    path('accessory/not_handled/<int:accessory_id>', accessory_not_handled, name='accessory_not_handled'),
    path('accessory/to_delivery/<int:apartment_id>', accessories_to_delivery, name='accessories_to_delivery'),
    path('accessory/to_not_handled/<int:accessory_id>', accessory_to_not_handled, name='accessory_to_not_handled'),
]
