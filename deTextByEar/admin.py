from django.contrib import admin
from django import forms
from .models import DeTextByEar
from django.db import models


@admin.register(DeTextByEar)
class AudioStoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'translation_text', 'keywords', 'translation_keywords', 'audio', 'level')
    search_fields = ('title', 'text', 'translation_text')
    formfield_overrides = {
        models.FileField: {'widget': forms.FileInput(attrs={'accept': 'audio/*'})},
    }
