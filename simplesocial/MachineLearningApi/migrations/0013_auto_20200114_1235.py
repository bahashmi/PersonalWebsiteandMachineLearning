# Generated by Django 2.1.5 on 2020-01-14 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MachineLearningApi', '0012_delete_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csvfile',
            name='id',
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]