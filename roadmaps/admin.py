from django.contrib import admin
from .models import Roadmap, RoadmapImage

class RoadmapImageInline(admin.TabularInline):
    model = RoadmapImage
    extra = 1  # Allows adding extra image entries in the inline form
    fields = ['image', 'image_no', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    show_change_link = True

class RoadmapAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at', 'updated_at']
    search_fields = ['title', 'description']
    list_filter = ['created_at', 'updated_at']
    inlines = [RoadmapImageInline]  # Inline for RoadmapImage

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'steps', 'resource_url')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ['created_at', 'updated_at']

admin.site.register(Roadmap, RoadmapAdmin)

class RoadmapImageAdmin(admin.ModelAdmin):
    list_display = ['roadmap', 'image_no', 'created_at', 'updated_at']
    list_filter = ['roadmap', 'created_at']
    search_fields = ['roadmap__title']
    readonly_fields = ['created_at', 'updated_at']

admin.site.register(RoadmapImage, RoadmapImageAdmin)
