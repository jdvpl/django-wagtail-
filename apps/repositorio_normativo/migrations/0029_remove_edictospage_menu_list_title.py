# Generated by Django 3.1.13 on 2022-03-09 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repositorio_normativo', '0028_auto_20220308_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edictospage',
            name='menu_list_title',
        ),
    ]