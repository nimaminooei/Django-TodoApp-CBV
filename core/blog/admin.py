from django.contrib import admin

# from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import post ,Comment,category


class customtask(admin.ModelAdmin):
    model = post
    list_display = ("author", "title","published_date")
    # list_filter = ("status",)
    fieldsets = (("fields", {"fields": ( "content","title","category","author")}),)
    add_fieldsets = (
        (None, {"Add post": ("wide",), "fields": ("author","title","category", "content")}),
    )
    search_fields = ("author", "title")
    ordering = ("published_date",)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at')
    list_filter = ('post', 'author','created_at')
    search_fields = ('text', 'author')

class categoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(category, categoryAdmin)
admin.site.register(post, customtask)
admin.site.register(Comment, CommentAdmin)
