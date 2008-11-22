from django.contrib import admin
from django_beer.models import Fermentable, Hop, Yeast

class FermentableAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
class HopAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class YeastAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Hop, HopAdmin)
admin.site.register(Fermentable, FermentableAdmin)
admin.site.register(Yeast, YeastAdmin)
