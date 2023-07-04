from django.db import models

# Create your models here.
class MyModel(models.Model):
    Date = models.DateField()
    Day = models.CharField(max_length=100, null = True,blank = True)
    Cars = models.IntegerField(null = True, blank= True)
    Scooters = models.IntegerField(null = True, blank= True)
    Tempo_Auto = models.IntegerField(null = True, blank= True)
    Cycles = models.IntegerField(null = True, blank= True)
    Buses = models.IntegerField(null = True, blank= True)
    Tractor_Trolley = models.IntegerField(null = True, blank= True)
    Others = models.CharField(max_length=200, null = True, blank= True)

    