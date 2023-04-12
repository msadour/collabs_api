from django.contrib import admin

from source.endpoints.security.models import IPBanned

admin.site.register(IPBanned)
