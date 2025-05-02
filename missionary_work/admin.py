from django.contrib import admin
from .models import MissionaryPhoto

class MissionaryPhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'category', 'date_taken', 'featured')
    list_filter = ('location', 'category', 'date_taken', 'featured')
    search_fields = ('title', 'description', 'location', 'category')
    date_hierarchy = 'date_taken'

admin.site.register(MissionaryPhoto, MissionaryPhotoAdmin)
