from django.contrib import admin
from .models import Data

# Register your models here.
class DataAdmin(admin.ModelAdmin):
    list_display=('name','age','sex','chestpaintype','restingbp','cholestrol','fastingbs','maxHR','exerciseangina','oldpeak','stslope','predictions')
admin.site.register(Data,DataAdmin)