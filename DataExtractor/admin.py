from django.contrib import admin
from .models import *

# Register your models here.

class NoDeleteAdminMixin:
    def has_delete_permission(self, request, obj=None):
        #return False # Disable Delete
        return True   # Enable Delete

class Feedback(NoDeleteAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'user', 'time', 'x', 'y', 'z')
    list_filter = ('user', 'time', 'x', 'y', 'z')
    search_fields = ('user', 'time', 'x', 'y', 'z')
admin.site.register(feedback,Feedback)
