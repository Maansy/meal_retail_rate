from django.contrib import admin
from .models import Meal , Rating
# Register your models here.

class RatingAdmin(admin.ModelAdmin):
    list_display = ('meal', 'user', 'stars')
    list_filter = ['meal', 'user']
    search_fields = ['meal', 'user']

class MealAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ['title', 'description']
    list_filter = ['title', 'description']



admin.site.register(Meal, MealAdmin)
admin.site.register(Rating, RatingAdmin)
