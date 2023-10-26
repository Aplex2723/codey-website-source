from django.contrib import admin
from .models import Project, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', ('updated'))

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('title', 'client', 'project_date', 'post_categories')
    ordering = ('title', 'project_date')
    search_fields = ('title', 'categories__name', 'client')

    #Creando nuevos campos
    def post_categories(self, obj):
        return ", ".join(c.name for c in obj.categories.all().order_by("name")) 
    post_categories.short_description = "Categorias"


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)