from django.contrib import admin
from .models import *

admin.site.register(Home)
admin.site.register(Stats)
admin.site.register(BlogCategory)
admin.site.register(BlogPost)
admin.site.register(TeamMember)


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    search_fields = ('title',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('category__title',)

# admin.site.register(FAQ)
# admin.site.register(Contact)
