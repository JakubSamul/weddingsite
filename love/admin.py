from django.contrib import admin

from .models import Guests, Side, Confirmation, Preferences

# Register your models here.

admin.site.register(Guests)
admin.site.register(Confirmation)
admin.site.register(Side)
admin.site.register(Preferences)

