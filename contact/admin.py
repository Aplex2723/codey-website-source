from django.contrib import admin
from .models import ConctactModel

# Register your models here.
@admin.register(ConctactModel)
class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'subject', 'created', 'content')
    list_display = ('name', 'email', 'subject', 'created')
    list_filter = ('created',)
    search_fields = ('name', 'email', 'content', 'subject')

