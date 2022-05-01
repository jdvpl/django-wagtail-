# Generated by Django 3.1.7 on 2021-04-09 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailmenus', '0023_remove_use_specific'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ministerio', '0003_auto_20210409_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstructuraSectorPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RenameModel(
            old_name='MisionVisionPage',
            new_name='CulturaCorporativaPage',
        ),
    ]