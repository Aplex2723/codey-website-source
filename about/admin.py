from django.contrib import admin
from .models import HTMLModel, Testimonials

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    pass

@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    readonly_fields = ('full_name', 'score', 'comments')

admin.site.register(HTMLModel, PageAdmin)
