from django.contrib import admin
from .models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'submitter', 'species', 'sex', 'age')
    list_filter = ('sex',)
    search_fields = ('name', 'submitter')