from django.contrib import admin
from .models import Tag,Project,ProjectImage

class ProjectImageInline(admin.TabularInline): # bang cham quan tri vien

    model = ProjectImage #che do xem co the tai len 1 anh
    extra = 1 #user tai len 1 anh
    
class ProjectAdmin(admin.ModelAdmin): #display admin
    list_display = ("title","link")
    inlines=[
        ProjectImageInline
    ]
    search_fields=("title","description")
    list_filter = ("tags",)

class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",) #lie ke de tim kiem
    
# step dang ky

admin.site.register(Tag,TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)