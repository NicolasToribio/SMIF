from django.contrib import admin
from .models import Tag, Project, ProjectImage #We have to register our models


class ProjectImageInline(admin.TabularInline):
  model = ProjectImage
  extra = 1 #by default, we ask the user to upload 1 image.


class ProjectAdmin(admin.ModelAdmin):
  list_display = ("title", "link")#When looking at a list of projects, we can see the title and link for those projects
  inlines = [ProjectImageInline]
  search_fields = ("title", "description")
  list_filter = ("tags",) #trailing comma added so that it gets treated like a tuple, and the parentheses don't auto delete and only leave the quotation marks and text


class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
