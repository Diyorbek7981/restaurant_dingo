from django.contrib import admin
from .models import *


@admin.register(FoodModel)
class FoodModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'about', 'price', 'created']
    list_display_links = ['title', 'about']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'created']

@admin.register(Chefs)
class ChefsAdmin(admin.ModelAdmin):
    list_display = ['full_name']

@admin.register(ChefLevel)
class ChefLevelAdmin(admin.ModelAdmin):
    list_display = ['ch_level']


@admin.register(BookingModel)
class BookingModelAdmin(admin.ModelAdmin):
    list_display = ['name','fone_number','num_of_g','date','time']
    list_display_links = ['name','date','time']
    list_filter = ['name','date','time']
    search_fields = ['name']


@admin.register(TagsModel)
class TagsModelAdmin(admin.ModelAdmin):
    list_display = ['tags']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'subject', 'create']
    list_display_links = ['name', 'phone', 'subject']
    list_filter = ['name', 'create']
    search_fields = ['name']


