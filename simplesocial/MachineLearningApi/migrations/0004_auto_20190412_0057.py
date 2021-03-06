# Generated by Django 2.1.5 on 2019-04-12 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MachineLearningApi', '0003_auto_20190411_0136'),
    ]

    operations = [
        migrations.AddField(
            model_name='csvfile',
            name='Appliances',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='Press_mm_hg',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='RH_1',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='RH_2',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='RH_3',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='RH_4',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='RH_5',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='RH_6',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='RH_7',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='RH_8',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='RH_9',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='RH_out',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='T1',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='T2',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='T3',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='T4',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='T5',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='T6',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='T7',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='T8',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='T9',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='T_out',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='Tdewpoint',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='Visibility',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='Windspeed',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='lights',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='rv1',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='rv2',
            field=models.FloatField(default=0),
        ),
    ]
