from django.contrib import admin

from .models import Animal
from .models import Municipality
from .models import Complaint
from .models import Ong

admin.site.register(Animal)
admin.site.register(Municipality)
admin.site.register(Ong)
admin.site.register(Complaint)
