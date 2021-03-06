# Generated by Django 2.1.5 on 2019-04-11 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSVFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('name', models.CharField(max_length=100)),
                ('Appliances', models.IntegerField()),
                ('lights', models.IntegerField()),
                ('T1', models.FloatField()),
                ('RH_1', models.FloatField()),
                ('T2', models.FloatField()),
                ('RH_2', models.FloatField()),
                ('T3', models.FloatField()),
                ('RH_3', models.FloatField()),
                ('T4', models.FloatField()),
                ('RH_4', models.FloatField()),
                ('T5', models.FloatField()),
                ('RH_5', models.FloatField()),
                ('T6', models.FloatField()),
                ('RH_6', models.FloatField()),
                ('T7', models.FloatField()),
                ('RH_7', models.FloatField()),
                ('T8', models.FloatField()),
                ('RH_8', models.FloatField()),
                ('T9', models.FloatField()),
                ('RH_9', models.FloatField()),
                ('T_out', models.FloatField()),
                ('Press_mm_hg', models.FloatField()),
                ('RH_out', models.FloatField()),
                ('Windspeed', models.FloatField()),
                ('Visibility', models.FloatField()),
                ('Tdewpoint', models.FloatField()),
                ('rv1', models.FloatField()),
                ('rv2', models.FloatField()),
            ],
        ),
    ]
