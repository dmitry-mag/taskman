from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    pass
    # fields = [list of fields]


admin.site.register(Task, TaskAdmin)