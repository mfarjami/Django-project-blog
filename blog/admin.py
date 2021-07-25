from django.contrib import admin
from .models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["position",  "title","parent", "slug", "status"]
    list_filter = ["status"]
    search_fields = ["title", "slug"]
    prepopulated_fields = {'slug':('title',)}
    

admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_editable = ["status", "author", "is_special"]
    list_display = ["title",  "image_tag","slug", "author","publish", "is_special","status", "category_to_str"]
    list_filter = ["publish","status", "author"]
    search_fields = ["title", "body"]
    prepopulated_fields = {'slug':('title',)}


admin.site.register(Article, ArticleAdmin)