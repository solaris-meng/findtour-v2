from django.contrib import admin

from .models import FormTestModel
from .models import PrivateTourFormModel
# Register your models here.
admin.site.register(FormTestModel)
admin.site.register(PrivateTourFormModel)
