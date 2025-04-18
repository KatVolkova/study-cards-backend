# Generated by Django 5.2 on 2025-04-17 22:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_cards', '0003_reviewhistory_streak'),
    ]

    operations = [
        migrations.AddField(
            model_name='flashcard',
            name='next_review_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='flashcard',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('reviewing', 'Reviewing'), ('mastered', 'Mastered')], default='new', max_length=20),
        ),
    ]
