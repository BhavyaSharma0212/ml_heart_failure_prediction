from django.urls import path
from .import views
urlpatterns =[
    path('',views.index, name='predictor-index'),
    path('predictions/',views.predictions, name='predictor-predictions'),
]