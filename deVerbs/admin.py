from django.contrib import admin
from django import forms
from .models import VerbWord
from django.db import models


@admin.register(VerbWord)
class VerbWordAdmin(admin.ModelAdmin):
    list_display = ('word', 'image', 'translation', 'verb', 'prefix')
    search_fields = ('word', 'translation', 'verb')
    formfield_overrides = {
        models.FileField: {'widget': forms.FileInput(attrs={'accept': 'image/*'})},
    }

