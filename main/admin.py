from django.contrib import admin
from main.models import Apartment
from accounts.models import CustomUser


class ApartmentAdmin(admin.ModelAdmin):
    exclude = ('slug',)


admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(CustomUser)
