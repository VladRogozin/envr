from django.db import models


class DeMessagesReply(models.Model):
    message_original = models.TextField(max_length=1000, default='none')
    message_translated = models.TextField(max_length=1000, default='none')
    hint = models.TextField(max_length=1000, default='none')
    background_original = models.TextField(max_length=1000, default='none')
    background_translated = models.TextField(max_length=1000, default='none')
    word_level = models.CharField(max_length=2, default='none')

    def __str__(self):
        return f"{self.background_original}"
