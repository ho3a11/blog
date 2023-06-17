from django.contrib import admin
from .models import Post, Category

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'parent')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category')
    search_fields = ('title', 'content')
    list_filter = ('author', 'category')

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
