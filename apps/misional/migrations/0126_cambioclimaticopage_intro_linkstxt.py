# Generated by Django 3.1.13 on 2022-03-24 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misional', '0125_auto_20220323_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='cambioclimaticopage',
            name='intro_linkstxt',
            field=models.TextField(blank=True, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', verbose_name='Texto introductorio'),
        ),
    ]