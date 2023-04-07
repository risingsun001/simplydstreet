from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    pass

@admin.register(Security)
class SecurityAdmin(admin.ModelAdmin):
    pass

@admin.register(SecurityMeta)
class SecurityMetaAdmin(admin.ModelAdmin):
    pass
