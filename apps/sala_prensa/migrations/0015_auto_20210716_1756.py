# Generated by Django 3.1.7 on 2021-07-16 22:56

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('sala_prensa', '0014_auto_20210715_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticiapage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', label='Bloque de párrafo', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(form_classname='title', label='Título', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(label='Imagen', required=True)), ('paragraph_block', wagtail.core.blocks.RichTextBlock(label='Texto de la imagen', required=True)), ('text', wagtail.core.blocks.TextBlock(label='Cita', required=False))], label='Bloque de imagen')), ('block_quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock(label='Cita')), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='Ej. Mary Berry', required=False))], label='Bloque de citación')), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-link', label='Bloque de enalce', template='news_blocks/embed_block.html'))], blank=True, verbose_name='Cuerpo de la noticia'),
        ),
    ]