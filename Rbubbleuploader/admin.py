from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Section)
admin.site.register(Product)
admin.site.register(Post)
admin.site.register(Photo)
admin.site.register(Photo2)

@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    ordering = ('title',)