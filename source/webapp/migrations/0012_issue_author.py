# Generated by Django 4.0.2 on 2022-03-04 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0011_project_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='issues', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]
