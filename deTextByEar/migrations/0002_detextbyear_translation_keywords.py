# Generated by Django 5.0.1 on 2024-01-30 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deTextByEar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detextbyear',
            name='translation_keywords',
            field=models.CharField(default='null', max_length=100),
        ),
    ]
