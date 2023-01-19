from django.contrib import admin

from .models import Address, LocationProduct, LocationProposition


admin.site.register(Address)
admin.site.register(LocationProduct)
admin.site.register(LocationProposition)
