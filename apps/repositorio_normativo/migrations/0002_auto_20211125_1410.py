# Generated by Django 3.1.13 on 2021-11-25 19:10

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0013_auto_20211125_1214'),
        ('repositorio_normativo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conceptopage',
            name='city',
        ),
        migrations.RemoveField(
            model_name='conceptopage',
            name='date_published',
        ),
        migrations.RemoveField(
            model_name='conceptopage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='conceptopage',
            name='introduction',
        ),
        migrations.RemoveField(
            model_name='conceptopage',
            name='tags',
        ),
        migrations.AddField(
            model_name='conceptopage',
            name='norm',
            field=models.TextField(blank=True, help_text='Normas/Jurisprudencia', verbose_name='Normas/Jurisprudencia'),
        ),
        migrations.AddField(
            model_name='conceptopage',
            name='norm_abolish',
            field=models.TextField(blank=True, help_text='Norma Derogada', verbose_name='Normas/Jurisprudencia'),
        ),
        migrations.AddField(
            model_name='conceptopage',
            name='petitioner',
            field=models.TextField(blank=True, help_text='Peticionario', verbose_name='Peticionario'),
        ),
        migrations.AddField(
            model_name='conceptopage',
            name='settled_date',
            field=models.DateField(null=True, verbose_name='Fecha de radicado'),
        ),
        migrations.AddField(
            model_name='conceptopage',
            name='settled_number',
            field=models.CharField(blank=True, max_length=255, verbose_name='Número de Radicado'),
        ),
        migrations.AddField(
            model_name='conceptopage',
            name='subject',
            field=models.TextField(blank=True, help_text='Tema', verbose_name='Tema'),
        ),
        migrations.AddField(
            model_name='conceptopage',
            name='summary',
            field=models.TextField(blank=True, help_text='Resumen', verbose_name='Resumen'),
        ),
        migrations.CreateModel(
            name='ConceptoAnoRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='concepto_year_relationship', to='repositorio_normativo.conceptopage')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='year_concepto_relationship', to='common.year')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]