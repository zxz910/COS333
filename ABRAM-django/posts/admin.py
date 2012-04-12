from posts.models import Thread, Post, Tag
from django.contrib import admin

class PostsInLine(admin.TabularInline):
	model = Post
	verbose_name = 'Posts'
	extra = 3

class TagsInLine(admin.TabularInline):
	model = Thread.tags.through
	verbose_name = 'Tags'
	verbose_name_plural = 'Tags'
	extra = 3

class ThreadAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['title']}),
		(None, {'fields': ['author']}),
	]
	inlines = [
		TagsInLine,
		PostsInLine
		]
	
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Tag)
admin.site.register(Post)