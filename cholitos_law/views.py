from django.shortcuts import render

from django.http import HttpResponse
from .models import Complaint
from .models import Animal
from .models import Municipality


def landing_page(request):
    complaints_list = Complaint.objects.all()
    animals_list = Animal.objects.all()
    municipalities_list = Municipality.objects.all()
    context = {
        'complaints_list' : complaints_list,
        'animals_list' : animals_list,
        'municipalities_list': municipalities_list,
    }
    return render(request, 'cholitos_law/landing_page.html', context)

def animal_record(request, animal_id):
    animals_list = Animal.objects.all()
    context = {
        'animals_list' : animals_list,
        'animal_id' : animal_id,
    }
    return render(request, 'cholitos_law/animal_record.html', context)

def complaint_record(request, complaint_id):
    complaints_list = Complaint.objects.all()
    context = {
        'complaints_list': complaints_list,
        'complaint_id' : complaint_id,
    }
    return render(request, 'cholitos_law/complaint_record.html', context)

def municipality_record(request, municipality_id):
    municipalities_list = Municipality.objects.all()
    context = {
        'municipalities_list': municipalities_list,
        'municipality_id' : municipality_id,
    }

    return render(request, 'cholitos_law/municipality_record.html', context)