# Generated by Django 3.1.13 on 2021-12-05 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('misional', '0079_auto_20211204_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='implementacionmisionpage',
            name='alt_text_one',
            field=models.TextField(blank=True, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', verbose_name='Texto alternativo'),
        ),
        migrations.AddField(
            model_name='implementacionmisionpage',
            name='alt_text_two',
            field=models.TextField(blank=True, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', verbose_name='Texto alternativo'),
        ),
        migrations.AddField(
            model_name='implementacionmisionpage',
            name='image_one',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen'),
        ),
        migrations.AddField(
            model_name='implementacionmisionpage',
            name='image_two',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen'),
        ),
        migrations.AddField(
            model_name='implementacionmisionpage',
            name='infographic_button_title',
            field=models.CharField(blank=True, help_text='Título del botón más información que será presentado al público, longitud máxima 20 caracteres', max_length=20, null=True, verbose_name='Título botón más información'),
        ),
        migrations.AddField(
            model_name='implementacionmisionpage',
            name='link',
            field=models.URLField(blank=True, verbose_name='Link del sitio'),
        ),
        migrations.AddField(
            model_name='implementacionmisionpage',
            name='link_video',
            field=models.URLField(blank=True, help_text='Si completa este campo, la imagen no será presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85', verbose_name='Video'),
        ),
        migrations.AddField(
            model_name='implementacionmisionpage',
            name='link_video_two',
            field=models.URLField(blank=True, help_text='Si completa este campo, la imagen no será presentada. El link requerido debe tener el siguiente formato https://www.youtube.com/embed/lkizzbz2ci85', verbose_name='Video'),
        ),
    ]