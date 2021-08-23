from django.contrib import admin

from .models import Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_on', 'updated_on']
    search_fields = ['title']


admin.site.register(Article, ArticleAdmin)
