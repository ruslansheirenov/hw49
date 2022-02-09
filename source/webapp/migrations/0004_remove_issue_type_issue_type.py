# Generated by Django 4.0.2 on 2022-02-09 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_statusmodel_statuses_alter_typemodel_types'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='type',
        ),
        migrations.AddField(
            model_name='issue',
            name='type',
            field=models.ManyToManyField(blank=True, related_name='issues', to='webapp.TypeModel'),
        ),
    ]