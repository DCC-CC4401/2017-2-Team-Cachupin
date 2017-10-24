from django.shortcuts import render

from django.http import HttpResponse
from .models import Complaint
from .models import Animal
from .models import Municipality
from datetime import datetime, timedelta


def landing_page(request):
    complaints_list = Complaint.objects.all()
    animals_list = Animal.objects.all()
    municipalities_list = Municipality.objects.all()
    context = {
        'complaints_list': complaints_list,
        'animals_list': animals_list,
        'municipalities_list': municipalities_list,
    }
    return render(request, 'cholitos_law/landing_page.html', context)


def animal_record(request, animal_id):
    animals_list = Animal.objects.all()

    try:
        this_animal = Animal.objects.get(pk=animal_id)
    except Exception:
        this_animal = None

    animal_is_none = this_animal.__class__ == None.__class__



    context = {
        'animals_list' : animals_list,
        'animal_id' : animal_id,
        'this_animal': this_animal,
        'age': datetime.today() - Animal.objects.get(pk=animal_id).birth.replace(tzinfo=None)
        if not animal_is_none else 0,
        'time': datetime.today() - Animal.objects.get(pk=animal_id).pub_date.replace(tzinfo=None)
        if not animal_is_none else 0,
    }
    return render(request, 'cholitos_law/animal_record.html', context)


def complaint_record(request, complaint_id=''):
    complaints_list = Complaint.objects.all()

    this_complaint = Complaint.objects.get(pk=complaint_id) if complaint_id !='' else None

    context = {
        'complaints_list': complaints_list,
        'complaint_id': complaint_id,
        'this_complaint':this_complaint,
        'Complaint': Complaint,
    }
    return render(request, 'cholitos_law/complaint_record.html', context)


def municipality_record(request, municipality_id):
    municipalities_list = Municipality.objects.all()
    context = {
        'municipalities_list': municipalities_list,
        'municipality_id': municipality_id,
    }

    return render(request, 'cholitos_law/municipality_record.html', context)

# def login(request):
#     return render(request, 'cholitos_law/templates/registration/login.html')

# def register(request):
#     return render(request, 'cholitos_law/register.html')