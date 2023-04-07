from django.db import models

# Create your models here.
class Exchange(models.Model):
    mic = models.CharField('MIC code', unique=True, max_length=20)
    name = models.CharField('Name of Stock Exchange', max_length=200)
    acronym = models.CharField('Acronym', max_length=15)
    country = models.CharField('Country', max_length=25)
    currency = models.CharField('Market Currency', max_length=3)
    timezone = models.CharField('TimeZone', max_length=35)

class Security(models.Model):
    symbol = models.CharField('Symbol', max_length=20)
    mic = models.ForeignKey(Exchange, related_name='securities', on_delete=models.CASCADE)
    isin = models.CharField('ISIN Number', max_length=15)
    name = models.CharField('Name of Company', max_length=200)
    instrument = models.CharField('Instrument', max_length=5)
    
    class Meta:
        unique_together = ('symbol', 'mic', 'instrument')
        verbose_name_plural = "securities"

class SecurityMeta(models.Model):
    security = models.ForeignKey(Security, related_name='meta', on_delete=models.CASCADE)
    column = models.CharField('Name of Data', max_length=100)
    dtype = models.CharField('Data Type', max_length=5)
    value = models.TextField('Data Value')