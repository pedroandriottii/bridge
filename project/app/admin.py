from django.contrib import admin
from .models import User, Project, RegionEnum, StatusEnum

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'get_region_display')

admin.site.register(User, UserAdmin)
admin.site.register(Project)
