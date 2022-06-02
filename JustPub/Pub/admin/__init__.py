from django.contrib import admin
from django.contrib.admin import ModelAdmin

from Pub.models import Category, DishesType, Dish
from .admin_forms import CategoryAdminForm, DishesTypeAdminForm, DishAdminForm


class CategoryAdmin(ModelAdmin):
    form = CategoryAdminForm


class DishesTypeAdmin(ModelAdmin):
    form = DishesTypeAdminForm


class DishAdmin(ModelAdmin):
    form = DishAdminForm


admin.site.register(Category, CategoryAdmin)
admin.site.register(DishesType, DishesTypeAdmin)
admin.site.register(Dish, DishAdmin)
