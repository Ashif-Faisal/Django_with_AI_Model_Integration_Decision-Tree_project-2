from django import forms


class PredictionForm(forms.Form):
    class Meta:
        fields = ['height','weight', 'shoe_size']
