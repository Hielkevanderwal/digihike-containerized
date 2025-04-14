from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    exclude = []

@admin.register(RouteSection)
class RouteSelectionAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ["section_name", "ordering"]

@admin.register(RouteProgress)
class RouteProgressAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ["team", "progress"]

@admin.register(HintUsed)
class HintUsedAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ["team", "route_section"]