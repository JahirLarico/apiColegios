# Generated by Django 4.2.1 on 2023-05-06 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_estudiantes_aporedados'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiantes',
            name='aporedados',
        ),
    ]