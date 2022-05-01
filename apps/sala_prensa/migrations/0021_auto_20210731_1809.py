# Generated by Django 3.1.7 on 2021-07-31 23:09

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('sala_prensa', '0020_infografiaautorrelationship_infografiaindexpage_infografiapage_infografiapagetag_sectorrelationship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infografiapage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Solo modo horizontal; ancho horizontal entre 1000px y 3000px.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Infografía'),
        ),
        migrations.AlterField(
            model_name='infografiapage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='sala_prensa.InfografiaPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]