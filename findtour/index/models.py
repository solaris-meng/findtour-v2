from django.db import models

# Create your models here.
class FormTestModel(models.Model):
    fname = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.fname

class PrivateTourFormModel(models.Model):
    fname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    destination_beijing = models.BooleanField(default=False)
    destination_shanghai = models.BooleanField(default=False)
    destination_xian = models.BooleanField(default=False)
    destination_luoyang = models.BooleanField(default=False)
    destination_dunhuang = models.BooleanField(default=False)
    destination_urumqi = models.BooleanField(default=False)
    destinaiton_other = models.BooleanField(default=False)

    car = models.CharField(max_length=100)
    departure = models.CharField(max_length=100)
    nights = models.CharField(max_length=100)

    age_18_39 = models.BooleanField(default=False)
    age_40_50 = models.BooleanField(default=False)
    age_51_65 = models.BooleanField(default=False)
    age_65 = models.BooleanField(default=False)

    service_advise = models.BooleanField(default=False)
    service_luxury = models.BooleanField(default=False)
    service_activity = models.BooleanField(default=False)
    service_guide = models.BooleanField(default=False)
    service_transfer = models.BooleanField(default=False)

    itinerary = models.TextField(max_length=1024, default='tmp')


    def __str__(self):
        return self.fname
