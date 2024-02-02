from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from post.models import Post, Comment, HashTag


# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "title", "rate", "created_at", "updated_at"]
    list_display_links = ["id", "title"]
    search_fields = ["title", "content"]
    list_filter = ["created_at", "updated_at"]
    list_editable = ["rate"]
    fields = ["id", "user",  "title", "content", "photo", "hashtags", "rate", "created_at", "updated_at"]
    readonly_fields = ["id", "created_at", "updated_at"]

    # def get_readonly_fields(self, request, obj=None):
    #     readonly_fields = super().get_readonly_fields(request, obj)
    #     if obj.id % 2 == 0:
    #         readonly_fields.append("title")
    #     return readonly_fields

    # def has_add_permission(self, request: HttpRequest) -> bool:
    #     if request.user.is_superuser:
    #         return True
    #     return False
    
    # def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
    #     return False
    
    # def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
    #     return False

    # def get_queryset(self, request: HttpRequest) -> QuerySet:
    #     qs = super().get_queryset(request)
    #     return qs.filter(id__in=[1, 2, 3])
    

admin.site.register(Comment)
admin.site.register(HashTag)
