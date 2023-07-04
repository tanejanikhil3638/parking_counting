from django.shortcuts import render

from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.contrib import messages
from datetime import datetime
from django.conf import settings
import csv
from .models import MyModel


def index(request):

    if request.method == 'POST':
        day = request.POST.get('Day')
        jeep = request.POST.get('cars')
        scooters = request.POST.get('scooters')
        Tempo_Auto = request.POST.get('Tempo_Auto')
        Cycles = request.POST.get('Cycles')
        Buses = request.POST.get('Buses')
        Tractor_Trolley = request.POST.get('Tractor_Trolley')
        Others = request.POST.get('Others')

        new = MyModel(Date=datetime.today(), Day=day, Cars=jeep, Scooters=scooters, Tempo_Auto=Tempo_Auto,
                      Cycles=Cycles, Buses=Buses, Tractor_Trolley=Tractor_Trolley, Others=Others)
        new.save()

    return render(request, "index.html")

MModel = MyModel.objects.all()
def export_to_csv(request):
  response = HttpResponse(content_type='text/csv')
  response['Content-Dispostion'] = 'attachment; filename = parking_export.csv'
  writer = csv.writer(response)
  
  writer.writerow(['Date', 'Day', 'Cars/Jeep', 'Scooters','Tempo/Auto', 'Cycles', 'Buses', 'Tractor/Trolley', 'others'])
  parking_fields = MModel.values_list(
        'Date', 'Day', 'Cars', 'Scooters', 'Tempo_Auto', 'Cycles', 'Buses', 'Tractor_Trolley', 'Others')
  for MyModel in parking_fields:
     writer.writerow(MyModel)
  return response
