from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    pass

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass
