from django import forms
from .models import MyModel

class MyForm(forms.ModelForm):
  class Meta:
    model = MyModel
    fields = [ "Cars", "Scooters","Tempo_Auto", "Cycles","Buses","Tractor_Trolley","Others"]
    labels = []