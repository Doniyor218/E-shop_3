from django.contrib import admin
from .models import Task
from .models import Resume

admin.site.register(Resume)
admin.site.register(Task)

