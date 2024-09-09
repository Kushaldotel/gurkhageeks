from django.contrib import admin

# Register your models here.
from .models import ProjectShowcaseImage, projectshowcase


class ProjectShowcaseAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "type_of_project", "technology_used"]
    ordering = ["-created_at"]
    fieldsets = [
        (
            "Project Imformation",
            {
                "fields": [
                    "name",
                    "type_of_project",
                    "description_of_project",
                    "Challenges_faced",
                    "suggestion",
                    "technology_used",
                    "project_link",
                    "user",
                ]
            },
        ),
        ("timestamp", {"fields": ["created_at"], "classes": ("collapse",)}),
    ]
    readonly_fields = ["created_at"]


admin.site.register(projectshowcase, ProjectShowcaseAdmin)
admin.site.register(ProjectShowcaseImage)
