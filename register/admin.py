from django.contrib import admin
from .models import School, Team
# Register your models here.

class SchoolAdmin(admin.ModelAdmin):
    search_fields = ['school']

class TeamAdmin(admin.ModelAdmin):
    list_display = ('team', 'school')
    list_filter = ['school']
    search_fields = ['team']

admin.site.register(School, SchoolAdmin)
admin.site.register(Team, TeamAdmin)
