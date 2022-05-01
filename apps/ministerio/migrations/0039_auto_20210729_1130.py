# Generated by Django 3.1.10 on 2021-07-29 11:30

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('ministerio', '0038_auto_20210723_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='procesosprocedimientospage',
            name='description',
            field=wagtail.core.fields.RichTextField(blank=True, help_text=None, null=True),
        ),
        migrations.AddField(
            model_name='procesosprocedimientospage',
            name='image',
            field=models.ForeignKey(help_text=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='procesosprocedimientospage',
            name='link_mapa',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='procesosprocedimientospage',
            name='systems',
            field=wagtail.core.fields.StreamField([('Procesos_y_Procedimientos', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(help_text=None, label=None, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text=None, label=None, required=True)), ('description', wagtail.core.blocks.TextBlock(help_text=None, label=None, required=True)), ('external_url', wagtail.core.blocks.URLBlock(help_text=None, label=None, required=False))]))], blank=True),
        ),
    ]