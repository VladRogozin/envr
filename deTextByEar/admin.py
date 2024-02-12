from django.contrib import admin
from django import forms
from .models import DeTextByEar, Playlist
from django.db import models


@admin.register(DeTextByEar)
class DeTextByEarAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'translation_text', 'audio', 'level')
    search_fields = ('title', 'text', 'translation_text')
    formfield_overrides = {
        models.FileField: {'widget': forms.FileInput(attrs={'accept': 'audio/*'})},
    }


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('audios',)
