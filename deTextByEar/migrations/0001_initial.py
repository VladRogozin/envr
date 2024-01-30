# Generated by Django 5.0.1 on 2024-01-30 17:05

import deTextByEar.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeTextByEar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('translation_text', models.TextField()),
                ('keywords', models.CharField(max_length=100)),
                ('audio', models.FileField(upload_to=deTextByEar.models.audio_file_name)),
                ('level', models.CharField(default='A2-B1', max_length=6)),
            ],
        ),
    ]