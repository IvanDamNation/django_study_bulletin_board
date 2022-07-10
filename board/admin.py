from django.contrib import admin

from .models import News, Category, Comment


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'author', 'content')
    list_editable = ('is_published', )
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'news', 'sender', 'text', 'created_at', 'accept')
    list_display_links = ('id', 'news', 'text')
    search_fields = ('news', 'sender', 'accept')
    list_editable = ('accept', )
    list_filter = ('accept', )


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
