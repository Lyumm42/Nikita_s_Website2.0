from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title' )
    list_display_links = ('id', 'title' )
    list_filter = ('id', 'title' )
    search_fields = ('id', 'title' )
    ordering = ('id', 'title' )