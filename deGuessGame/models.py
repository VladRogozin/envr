from django.db import models


class DeWord(models.Model):
    original_word = models.CharField(max_length=255, default='none')
    translated_word = models.CharField(max_length=255, default='none')
    auxiliary_words = models.JSONField(default=dict)
    word_level = models.CharField(max_length=2, default='none')

    def __str__(self):
        return f"{self.original_word} - {self.translated_word} ({self.word_level})"
