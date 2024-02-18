from django.db import models


class VerbWord(models.Model):
    word = models.CharField(max_length=100)  # Слово
    image = models.ImageField(upload_to='images/')  # Изображение
    translation = models.CharField(max_length=100)  # Перевод
    verb = models.CharField(max_length=100, default='none' )  # Слово
    prefix = models.CharField(max_length=100, default='none')

    def __str__(self):
        return self.word
