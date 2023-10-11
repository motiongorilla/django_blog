from django.contrib import admin
from .models import Post, Category, Comment


class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ["post"]

# adding search over posts and additional fields
class PostAdmin(admin.ModelAdmin):
    search_fields = ["title", "intro", "body"]
    list_display = ["title", "status", "created_at"]
    list_filter = ["category", "status"]
    inlines = [CommentItemInline]
    # autogenerates slug
    prepopulated_fields = {"slug":('title',)}

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title"]
    prepopulated_fields = {"slug":('title',)}

class CommentAdmin(admin.ModelAdmin):
    search_fields = ["name", "body"]
    list_display = ["name", "email", "body"]

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
