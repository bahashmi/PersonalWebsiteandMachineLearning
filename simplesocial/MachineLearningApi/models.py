from django.db import models
import pandas as pd

from django.db import models
class UserDetails(models.Model):

    changeTypeCol = models.CharField(max_length=100)
    changeColTypeTo = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.title

class dataCleaningModels(models.Model):
    changeTypeCol = models.CharField(max_length=100)
    changeColTypeTo = models.CharField(max_length=100)

class replaceNaNvaluesModels(models.Model):
     DropcolName = models.CharField(max_length=100)
     replacevaluesWith = models.IntegerField()
     valueToBeReplaced = models.IntegerField(max_length=100,default=0)
     Random_Shuffle = models.BooleanField(default=True)

      


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='media/downloaded')
    uploaded_at = models.DateTimeField(auto_now_add=True)

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
