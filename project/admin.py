from django.contrib import admin

from accessories.models import AccessoryType
from issues.models import IssueType
from project.models import Apartment
from accounts.models import User


class ApartmentAdmin(admin.ModelAdmin):
    exclude = ('slug', 'kitchen', 'rooms')


admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(User)
admin.site.register(IssueType)
admin.site.register(AccessoryType)
