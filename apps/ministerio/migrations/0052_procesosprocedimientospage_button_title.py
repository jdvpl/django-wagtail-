# Generated by Django 3.1.13 on 2021-09-28 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ministerio', '0051_auto_20210927_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='procesosprocedimientospage',
            name='button_title',
            field=models.CharField(default='boton', help_text='Título del boton', max_length=254, verbose_name='Título del boton'),
            preserve_default=False,
        ),
    ]