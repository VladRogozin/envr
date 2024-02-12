from django.db import models


def audio_file_name(instance, filename):
    new_filename = f"{instance.title}_textByEar.mp3"
    return f'audio/DE/DeTextByEar/{new_filename}'


class DeTextByEar(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    translation_text = models.TextField()
    audio = models.FileField(upload_to=audio_file_name)
    level = models.CharField(max_length=6, default='A2-B1')

    def __str__(self):
        return self.title

class Playlist(models.Model):
    name = models.CharField(max_length=255)
    audios = models.ManyToManyField(DeTextByEar)

    def __str__(self):
        return self.name
