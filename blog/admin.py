from django.contrib import admin
from .models import Category, Post, Comment

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', ('updated'))

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', ('updated'))
    list_display = ('title', 'author', 'published', 'post_categories') #Muestra en la lista los valores establecidos
    ordering = ('author', 'published') # Ordena la lista dependiendo los valores
    search_fields = ('title', 'categories__name') #El cmapo no puede quear como 'author' ya que es un modelo relacionado
    date_hierarchy = 'published' # Gerarquizar los filtros mediante las fechas
    list_filter = ( 'categories__name',) # Creacion de filtros

    #Creando nuevos campos
    def post_categories(self, obj):
        return ", ".join(c.name for c in obj.categories.all().order_by("name")) 
    post_categories.short_description = "Categorias"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'post', 'created', 'active')
    list_filter = ('active', 'created')
    search_fields = ('name', 'email', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, querry):
        querry.update(active=True)