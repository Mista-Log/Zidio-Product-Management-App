from django.contrib import admin
# from .models import Project
# # Register your models here.
# admin.site.register(Project)


from django.contrib import admin
from .models import Client, Project, Task

admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Task)