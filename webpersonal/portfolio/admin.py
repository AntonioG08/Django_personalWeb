from django.contrib import admin
from .models import project


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    # With this we can put these elements from the 'models' section as readable
    readonly_fields = ('created', 'updated')


admin.site.register(project, ProjectAdmin)
