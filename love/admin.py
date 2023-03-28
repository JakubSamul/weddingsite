from django.contrib import admin

from .models import Guests

# Register your models here.
class GuestAdmin(admin.ModelAdmin):
    filter_horizontal = ('accompanying',)

admin.site.register(Guests,GuestAdmin)


