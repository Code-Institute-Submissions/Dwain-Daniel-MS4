from django.contrib import admin
from .models import Workouts, Category

# Register your models here.

class WorkoutsAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )




admin.site.register(Workouts, WorkoutsAdmin)
admin.site.register(Category, CategoryAdmin)