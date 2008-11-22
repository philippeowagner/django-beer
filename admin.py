from django.contrib import admin
from django_beer.models import Hop

class HopAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Hop, HopAdmin)