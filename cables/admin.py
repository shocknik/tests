from django.contrib import admin
from .models import Cable, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)

class CableAdmin(admin.ModelAdmin):
    list_display = ['mark']

admin.site.register(Cable, CableAdmin)
# Register your models here.
