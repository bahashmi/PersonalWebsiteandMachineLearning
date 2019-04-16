from django.db import models
import pandas as pd



# Create your models here.

# # Create your tests here.
class CSVFile(models.Model):
    name= models.CharField(max_length=100)
    Appliances = models.IntegerField(default=0)
    lights = models.IntegerField(default=0)
    T1 = models.FloatField(default=0)
    RH_1 = models.FloatField(default=0)
    T2 = models.FloatField(default=0)
    RH_2 = models.FloatField(default=0)

    T3 = models.FloatField(default=0)
    RH_3 = models.FloatField(default=0)
    T4 = models.FloatField(default=0)
    RH_4 = models.FloatField(default=0)

    T5 = models.FloatField(default=0)
    RH_5 = models.FloatField(default=0)
    T6 = models.FloatField(default=0)
    RH_6 = models.FloatField(default=0)

    T7 = models.FloatField(default=0)
    RH_7 = models.FloatField(default=0)
    T8 = models.FloatField(default=0)
    RH_8 = models.FloatField(default=0)

    T9 = models.FloatField(default=0)
    RH_9 = models.FloatField(default=0)

    T_out = models.FloatField(default=0)
    Press_mm_hg = models.FloatField(default=0)
    RH_out = models.FloatField(default=0)
    Windspeed = models.FloatField(default=0)
    Visibility = models.FloatField(default=0)
    Tdewpoint = models.FloatField(default=0)
    rv1 = models.FloatField(default=0)
    rv2 = models.FloatField(default=0)
