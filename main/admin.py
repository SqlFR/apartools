from django.contrib import admin

from issues.models import TypeIssue, Issue
from main.models import Apartment
from accounts.models import CustomUser


class ApartmentAdmin(admin.ModelAdmin):
    exclude = ('slug', 'kitchen', 'rooms')


admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(CustomUser)
admin.site.register(TypeIssue)
admin.site.register(Issue)
