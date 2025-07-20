from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Home, Stats, BlogCategory, BlogPost, TeamMember,
    Gallery, GalleryImage, GalleryCategory, BlogImages,FAQ
)

# Register other models simply
admin.site.register(Home)
admin.site.register(Stats)
admin.site.register(BlogCategory)

admin.site.register(TeamMember)
admin.site.register(FAQ)

# Inline for multiple images


class BlogPostImageInline(admin.TabularInline):
    model = BlogImages
    extra = 3
    readonly_fields = ['image_preview']
    fields = ['images', 'image_preview']

    def image_preview(self, obj):
        if obj.images:
            return format_html('<img src="{}" width="100" height="auto" />', obj.images.url)
        return "-"
    image_preview.short_description = "Preview"


class BlogPostAdmin(admin.ModelAdmin):
    inlines = [BlogPostImageInline]

admin.site.register(BlogPost, BlogPostAdmin)

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 3
    fields = ['image']
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="auto" />'
        return "-"
    image_preview.allow_tags = True
    image_preview.short_description = "Preview"

# Custom admin for Gallery
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('category__title',)
    inlines = [GalleryImageInline]

# Custom admin for GalleryCategory
@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    search_fields = ('title',)
