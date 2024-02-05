from django.contrib import admin
from .models import DeMessagesReply


@admin.register(DeMessagesReply)
class AudioStoryAdmin(admin.ModelAdmin):
    list_display = ('message_original', 'message_translated', 'hint', 'background_original', 'background_translated', 'word_level')
    search_fields = ('message_original', 'hint', 'background_original')
