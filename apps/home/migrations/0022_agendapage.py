# Generated by Django 3.1.13 on 2022-04-29 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('home', '0021_clasificadospage_solicitudespage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgendaPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('systems_title', models.CharField(blank=True, help_text='Titulo', max_length=120, null=True, verbose_name='Titulo')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]