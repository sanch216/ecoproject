from django.contrib import admin
from .models import Complaint, Volunteer

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'location', 'threat_level', 'status', 'created_at')
    list_filter = ('status', 'threat_level')
    search_fields = ('location', 'description')

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'cleaned_count')
