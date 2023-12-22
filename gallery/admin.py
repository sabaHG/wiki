from django.contrib import admin
from .models import Photo, Comment

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "image"]
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ["created"]

admin.site.register(Comment)