from django.db import models


class Spell(models.Model):
    word = models.JSONField()
    level = models.CharField(max_length=10, default='')
