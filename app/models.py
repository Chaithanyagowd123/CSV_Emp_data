from django.db import models

# Create your models here.
class Business_Employment_Data(models.Model):
    series_reference=models.CharField(max_length=100)
    period=models.DecimalField(max_digits=10,decimal_places=2)
    data_value=models.CharField(max_length=100)
    suppressed=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    units=models.CharField(max_length=100)
    magnitude=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    group=models.CharField(max_length=100)
    series_title_1=models.CharField(max_length=100)
    series_title_2=models.CharField(max_length=100)
    series_title_3=models.CharField(max_length=100)
    series_title_4=models.CharField(max_length=100)
    series_title_5=models.CharField(max_length=100)










    