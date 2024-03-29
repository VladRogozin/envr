# Generated by Django 5.0.1 on 2024-02-04 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeMessagesReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_original', models.TextField(default='none', max_length=1000)),
                ('message_translated', models.TextField(default='none', max_length=1000)),
                ('hint', models.TextField(default='none', max_length=1000)),
                ('background_original', models.TextField(default='none', max_length=1000)),
                ('background_translated', models.TextField(default='none', max_length=1000)),
                ('word_level', models.CharField(default='none', max_length=2)),
            ],
        ),
    ]
