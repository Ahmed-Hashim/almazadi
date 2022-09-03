from django.contrib import admin

# Register your models here.
from .models import Category, Post,Schedule,PublishedPost

admin.site.register(Post)

admin.site.register(Category)
admin.site.register(Schedule)
admin.site.register(PublishedPost)