from django.contrib import admin
# Register your models here.
from models import Article, Comment


class ArticleInline (admin.StackedInline):
    model = Comment
    extra = 2


class ArticleAdmin (admin.ModelAdmin):
    fields = ['Title','Text','Date','Pic','Category']
    inlines = [ArticleInline]
    list_filter = ['Date']

admin.site.register(Article,ArticleAdmin)