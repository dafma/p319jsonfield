from django.contrib import admin
from .models import Casa
# Register your models here.

@admin.register(Casa)
class CasaAdmin(admin.ModelAdmin):
    pass