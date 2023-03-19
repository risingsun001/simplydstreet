from django.db import models

# Create your models here.
class Exchange(models.Model):
    code = models.CharField('MIC code', primary_key=True, max_length=20)
    name = models.CharField('Name of Stock Exchange', max_length=15)
    country = models.CharField('Country', max_length=25)
    timezone = models.CharField('TimeZone', max_length=35)

class Stock(models.Model):
    symbol = models.CharField('Symbol', primary_key=True, max_length=20)
    mic_code = models.ForeignKey(Exchange, related_name='stocks', on_delete=models.CASCADE)
    name = models.CharField('Name of Stock', max_length=200)
    currency = models.CharField('Market Currency', max_length=3)
    stock_type = models.CharField('Stock Type', max_length=30)

