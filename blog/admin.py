from django.contrib import admin
from blog.models import Post, Tag, Comment


class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ('post', 'author')
    list_per_page = 20


class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('likes', 'author', 'tags')
    list_per_page = 20


class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
