# Generated by Django 3.0.6 on 2020-05-30 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MachineLearningApi', '0020_auto_20200403_0639'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='inputcols',
            new_name='changeColTypeTo',
        ),
        migrations.RenameField(
            model_name='userdetails',
            old_name='targetcols',
            new_name='changeTypeCol',
        ),
    ]
