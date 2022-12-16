"""Admin panel."""

from django.contrib import admin
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    """Class CategoryAdmin."""

    pass


admin.site.register(Product)
admin.site.register(Category, CategoryAdmin)
