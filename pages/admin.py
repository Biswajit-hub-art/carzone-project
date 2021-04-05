from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40"/>'.format(object.photo.url))

    thumbnail.short_description='Photo'
    fields=('first_name', 'designation', 'created_date')
    list_display=['id', 'thumbnail', 'first_name', 'designation', 'created_date']
    list_display_links=['id', 'first_name']
    search_fields=['first_name', 'designation', 'last_name']
    list_filter=['designation']

admin.site.register(Team, TeamAdmin)
