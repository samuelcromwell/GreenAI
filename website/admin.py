from django.contrib import admin
from .models import Contact, TeamMember

admin.site.register(Contact)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
