from django.contrib import admin

from accessories.models import AccessoryType
from issues.models import IssueType
from main.models import Apartment
from accounts.models import CustomUser


class ApartmentAdmin(admin.ModelAdmin):
    exclude = ('slug', 'kitchen', 'rooms')


admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(CustomUser)
admin.site.register(IssueType)
admin.site.register(AccessoryType)
