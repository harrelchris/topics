from django.contrib import admin

from . import models

admin.site.register(models.Category)
admin.site.register(models.Topic)
admin.site.register(models.Discussion)
admin.site.register(models.Comment)
