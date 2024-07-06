from django.contrib import admin
from .models import *


class MainPageDataAdmin(admin.ModelAdmin):
    list_display = ("img_url", 'text', 'email', 'tel_no')


admin.site.register(MainPageData, MainPageDataAdmin)


class ProjectsDoneAdmin(admin.ModelAdmin):
    list_display = ("img_url", "text")


admin.site.register(ProjectsDone, ProjectsDoneAdmin)