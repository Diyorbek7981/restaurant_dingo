from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']


@admin.register(Coments)
class ComentsAdmin(admin.ModelAdmin):
    list_display = ['user','message','created']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']


