from django.contrib import admin
from .models import Calendar, Project, Task, Reminder

# Register your models here.

admin.site.register(Calendar)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Reminder)