from django.contrib import admin

from .models import Animal
from .models import Municipality
from .models import Complaint

admin.site.register(Animal)
admin.site.register(Municipality)
admin.site.register(Complaint)