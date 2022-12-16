"""Admin panel."""

from django.contrib import admin
from .models import Proposition


admin.site.register(Proposition)
