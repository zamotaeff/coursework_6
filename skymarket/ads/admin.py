from django.contrib import admin

from ads.models import Ad, Comment


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'author', 'id')
    list_display_links = ('title',)
    list_filter = ('author', )
    list_editable = ('price', )
    search_fields = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('ad', 'author', 'id')
    list_filter = ('ad', 'author',)
    search_fields = ('author',)
