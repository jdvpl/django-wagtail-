# Generated by Django 3.1.13 on 2022-03-09 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repositorio_normativo', '0032_auto_20220309_0437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edictospage',
            name='menu_list',
        ),
        migrations.RemoveField(
            model_name='edictospage',
            name='menu_list_title',
        ),
    ]