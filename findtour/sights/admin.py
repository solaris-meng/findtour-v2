from django.contrib import admin

from .models import Area, Sight

# Register your models here.
class AreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_pic')

class SightAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'main_pic')
    list_filter = ['city']

admin.site.register(Area, AreaAdmin)
admin.site.register(Sight, SightAdmin)
