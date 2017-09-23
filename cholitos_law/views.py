from django.shortcuts import render

from django.http import HttpResponse


def landing_page(request):
    return HttpResponse("Landing Page")

def animal_record(request, animal_id):
    return HttpResponse("Estas buscando la ficha del animal %s." % animal_id)

def complaint_record(request, complaint_id):
    return HttpResponse("Estas buscando la ficha de denuncia numero %s." % complaint_id)

def municipality_record(request, municipality_id):
    return HttpResponse("Estas buscando la ficha de la municipalidad numero %s." % municipality_id)