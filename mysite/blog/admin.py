from django.contrib import admin
from .models import *


admin.site.register(BlogComment)
admin.site.register(BlogAuthor)

class BlogCommentsInline(admin.TabularInline):
    model = BlogComment
    max_num = 0

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blogtitle', 'blogdate', 'blogauthor')
    inlines = [BlogCommentsInline]
