from django.contrib import admin

from subscribe.models import Subscribe

class AdminSubscribe(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')

# Register your models here.
admin.site.register(Subscribe, AdminSubscribe)