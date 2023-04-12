from django.contrib import admin
from .models import Account, Industry, IPBanned


admin.site.register(Account)
admin.site.register(Industry)
admin.site.register(IPBanned)
