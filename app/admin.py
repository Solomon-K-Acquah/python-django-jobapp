from dataclasses import fields
from django.contrib import admin

from app.models import Author, JobPost, Location, Skills

# customizing django admin interface
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'salary', 'date')
    list_filter = ('date', 'salary', 'expiry')
    search_fields = ('title', 'description')
    search_help_text = "Write in your query and hit enter"
    # fields = (('title', 'description'), 'expiry')
    # exclude = ('salary',)
    fieldsets = (
        ('Basic information', {
            'fields': ('title', 'description')
        }),
        ('More information', {
            # 'classes': ('collapse', 'wide'),
            'fields': ('salary', 'expiry', 'slug', 'location', 'author', 'skills')
        })
    )

# Register your models here.
admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)
