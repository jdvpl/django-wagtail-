# Generated by Django 3.1.13 on 2021-09-30 20:39

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('wagtailimages', '0023_add_choose_permissions'),
        ('misional', '0007_auto_20210929_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuentesNoConvencionalesEnergiaRenovablePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro_title', models.CharField(default='Servicio al ciudadano', max_length=254, verbose_name='Título de la sección')),
                ('intro', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción')),
                ('alt_text', models.TextField(blank=True, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', verbose_name='Texto alternativo')),
                ('energy_list_title', models.CharField(blank=True, help_text='Título que será presentado al publico', max_length=255, null=True, verbose_name='Título de la sección')),
                ('energy_list', wagtail.core.fields.StreamField([('Energias', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Título del portafolio, políticas y/o protocolos de servicio ', label='Título', required=True)), ('main_description', wagtail.core.blocks.TextBlock(help_text='Descripción principal del portafolio, políticas y/o protocolos de servicio ', label='Descripción principal ', required=True)), ('second_description', wagtail.core.blocks.TextBlock(help_text='Descripción complementaria del portafolio, políticas y/o protocolos de servicio ', label='Descripción complementaria ', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(blank=False, help_text='Tamaño recomendado de la imagen 200px X 200px pixeles', label='Imagen', required=True)), ('alt_text', wagtail.core.blocks.TextBlock(blank=False, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', label='Texto alternativo', required=False))]))], blank=True, verbose_name='Energías renovables no convencionales')),
                ('second_intro_title', models.CharField(default='Servicio al ciudadano', max_length=254, verbose_name='Título de la sección')),
                ('second_intro', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción')),
                ('second_alt_text', models.TextField(blank=True, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', verbose_name='Texto alternativo')),
                ('sale_list_title', models.CharField(blank=True, help_text='Título que será presentado al publico', max_length=255, null=True, verbose_name='Título de la sección')),
                ('sale_list', wagtail.core.fields.StreamField([('Subastas', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Titulo del elemento', label='Titulo', required=True)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Descripción del elemento', icon='fa-paragraph', label='Descripción', required=True)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Complete este campo si desea enlazar este elemento con una página local', label='Link a página local', required=False)), ('external_url', wagtail.core.blocks.URLBlock(help_text='Complete este campo si desea enlazar este elemento con una página externa. Si este campo está completo, no se tendrá en cuenta el link a página local', label='Link a página externa', required=False))]))], blank=True, verbose_name='Subastas')),
                ('third_intro_title', models.CharField(default='Servicio al ciudadano', max_length=254, verbose_name='Título de la sección')),
                ('third_intro', wagtail.core.fields.RichTextField(blank=True, help_text='Introducción de la sección', null=True, verbose_name='Introducción')),
                ('third_alt_text', models.TextField(blank=True, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', verbose_name='Texto alternativo')),
                ('resource_list_title', models.CharField(blank=True, help_text='Título que será presentado al publico', max_length=255, null=True, verbose_name='Título de la sección')),
                ('resource_list', wagtail.core.fields.StreamField([('Recursos', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(help_text='Título del portafolio, políticas y/o protocolos de servicio ', label='Título', required=True)), ('main_description', wagtail.core.blocks.TextBlock(help_text='Descripción principal del portafolio, políticas y/o protocolos de servicio ', label='Descripción principal ', required=True)), ('second_description', wagtail.core.blocks.TextBlock(help_text='Descripción complementaria del portafolio, políticas y/o protocolos de servicio ', label='Descripción complementaria ', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(blank=False, help_text='Tamaño recomendado de la imagen 200px X 200px pixeles', label='Imagen', required=True)), ('alt_text', wagtail.core.blocks.TextBlock(blank=False, help_text='Este atributo proporciona información alternativa para una imagen si un usuario, por alguna razón, no puede verla (debido a una conexión lenta, un error en el atributo src o si el usuario utiliza un lector de pantalla)', label='Texto alternativo', required=False))]))], blank=True, verbose_name='Recursos Energéticos Distribuidos')),
                ('image', models.ForeignKey(blank=True, help_text='Imagen que representa la sección', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen')),
                ('second_image', models.ForeignKey(blank=True, help_text='Imagen que representa la sección', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen')),
                ('third_image', models.ForeignKey(blank=True, help_text='Imagen que representa la sección', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]