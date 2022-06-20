from django.contrib import admin
from apps.post.models import Category, Post, Tags
# Register your models here.


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Tags)