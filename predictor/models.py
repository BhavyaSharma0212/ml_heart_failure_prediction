from django.db import models
from sklearn.ensemble import RandomForestClassifier
import joblib
# Create your models here.
class Data(models.Model):
    class Sex(models.IntegerChoices):
        MALE = 1
        FEMALE = 0
    class Chestpaintype(models.IntegerChoices):
        ATYPICAL__ANGINA = 1
        TYPICAL_ANGINA = 3
        NON_ANGINAL_PAIN = 2
        ASYMPTOMATIC = 0
    class Restingecg(models.IntegerChoices):
        NORMAL = 1
        ST_ABNORMAL = 2
        LEFT_VENTRICULAR_HYPERTROPY = 0
    class Fastingbs(models.IntegerChoices):
        MORE_THAN_120 = 1
        OTHERWISE =0
    class Exerciseangina(models.IntegerChoices):
        YES = 1
        NO = 0
    class Stslope(models.IntegerChoices):
        UP = 2
        FLAT = 1
        DOWN =0

    name = models.CharField(max_length=100 , null = True)
    age = models.PositiveIntegerField(null = True)
    sex = models.IntegerField(choices=Sex.choices, null = True)
    chestpaintype = models.IntegerField(choices=Chestpaintype.choices, null = True)
    restingbp = models.PositiveIntegerField(null = True)
    cholestrol = models.PositiveIntegerField(null = True)
    fastingbs = models.IntegerField(choices=Fastingbs.choices, null = True)
    restingecg = models.IntegerField(choices=Restingecg.choices, null = True)
    maxHR = models.PositiveIntegerField(null = True)
    exerciseangina = models.IntegerField(choices=Exerciseangina.choices, null = True)
    oldpeak = models.FloatField(null = True)
    stslope =  models.IntegerField(choices=Stslope.choices, null = True)
    predictions = models.IntegerField( blank = True)
    date = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/heart_failure_model.joblib')
        self.predictions=ml_model.predict([[self.age,self.sex,self.chestpaintype,self.restingbp,self.cholestrol,self.fastingbs,self.restingecg,self.maxHR,self.exerciseangina,self.oldpeak,self.stslope]])
        return super().save(*args,**kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name