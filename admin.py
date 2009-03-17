from django.contrib import admin
from django_beer.models import Fermentable, Hop, Yeast, Misc, Water, Equipment, \
    Style, MashProfile, MashStep, Recipe

class FermentableAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
class HopAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class YeastAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class MiscAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class WaterAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class EquipmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class StyleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class MashProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class MashStepAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(MashStep, MashStepAdmin)
admin.site.register(MashProfile, MashProfileAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Water, WaterAdmin)
admin.site.register(Misc, MiscAdmin)
admin.site.register(Hop, HopAdmin)
admin.site.register(Fermentable, FermentableAdmin)
admin.site.register(Yeast, YeastAdmin)
