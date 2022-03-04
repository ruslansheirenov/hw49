# Generated by Django 4.0.2 on 2022-03-04 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0010_alter_project_created_at_alter_project_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='projects', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]