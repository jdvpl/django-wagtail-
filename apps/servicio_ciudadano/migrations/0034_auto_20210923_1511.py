# Generated by Django 3.1.13 on 2021-09-23 20:11

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('servicio_ciudadano', '0033_caracterizacionusuariospage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plananticorrucionpage',
            name='management_intro',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción'),
        ),
        migrations.AlterField(
            model_name='plananticorrucionpage',
            name='management_list',
            field=wagtail.core.fields.StreamField([('Items', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Titulo del elemento', label='Titulo', required=True)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción del elemento', icon='fa-paragraph', label='Descripción', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local', label='Link a página externa', required=False))]))], blank=True, verbose_name='Gestión Documental'),
        ),
    ]