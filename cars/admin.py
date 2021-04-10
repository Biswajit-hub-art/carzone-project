from django.contrib import admin
from .models import Car
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description= 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True

    list_display = ('id', 'thumbnail_preview', 'car_title', 'color', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links= ('id', 'thumbnail_preview', 'car_title')
    list_editable=('is_featured',)
    search_fields= ('id', 'car_title', 'color', 'fuel_type')
    list_filter= ('car_title', 'color', 'year', 'body_style', 'fuel_type')

admin.site.register(Car, CarAdmin)
