# Generated by Django 2.1.5 on 2020-09-25 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MachineLearningApi', '0025_replacenanvaluesmodels_random_shuffle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='replacenanvaluesmodels',
            old_name='colName',
            new_name='DropcolName',
        ),
    ]