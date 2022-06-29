from django.shortcuts import render,redirect
from .forms import DataForm
from .models import Data
# Create your views here.
def index(request):
    if request.method=='POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('predictor-predictions')
    else:
        form = DataForm()
    form = DataForm()
    context={
        'form' :form ,
    }
    return render(request, 'predictor/index.html',context)

def predictions(request):
    predicted_result = Data.objects.all()
    context={
        'predicted_result' : predicted_result
    }
    return render(request, 'predictor/predictions.html',context)