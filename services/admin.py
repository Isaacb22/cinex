from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	list_display = ('title', 'author', 'published')
	ordering = ('author', 'published','categories__name')
	search_fields = ('title','content','author__username', 'categories__name')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)