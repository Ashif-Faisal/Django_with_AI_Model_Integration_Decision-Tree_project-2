from django.http import HttpResponse
from django.shortcuts import render
from .forms import PredictionForm
import pandas as pd
import joblib


# Create your views here.
def predict(request):
    if request.method == "POST":
        form = PredictionForm(request.POST)
        if form.is_valid():
            height = request.POST.get('height')
            weight = request.POST.get('weight')
            shoe_size = request.POST.get('shoe_size')

            print(height, weight, shoe_size)

            df = pd.DataFrame({'height': [height], 'weight': [weight], 'shoe size': [shoe_size]})
            print(df)
            model = joblib.load('model_prediction/decision_tree_model.pkl')
            predicted_value = model.predict(df)
            print(predicted_value)

            if predicted_value[0]=='male':
                return HttpResponse('This guy is Male')
            else:
                return HttpResponse('This guy is Female')
    else:
        form = PredictionForm()
    return render(request, "predict.html", {"form": form})
