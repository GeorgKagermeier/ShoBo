"""
Admin module register modules which are accessible to the admin
"""
from django.contrib import admin
from .models import Story, Note, Comment


admin.site.register(Story)
admin.site.register(Note)
admin.site.register(Comment)