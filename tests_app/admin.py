from django.contrib import admin
from .models import Test, TestType


class TypeTestAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(TestType, TypeTestAdmin)


class TestAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'base_unit']
admin.site.register(Test, TestAdmin)
# Register your models here.
