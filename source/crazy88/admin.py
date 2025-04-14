from django.contrib import admin
from .models import MissionList, MissionExecution, Team

# Register your models here.
@admin.register(MissionExecution)
class MissionExecutionAdmin(admin.ModelAdmin):
    list_display = ["team","mission_list", "mission_number", "validated"]

admin.site.register(MissionList)