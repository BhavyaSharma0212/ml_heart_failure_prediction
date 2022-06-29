from django import forms
from .models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model=Data
        fields = ['name','age','sex','chestpaintype','restingbp','cholestrol','fastingbs','restingecg','maxHR','exerciseangina','oldpeak','stslope']