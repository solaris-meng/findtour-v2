
from django import forms
from django.forms import ModelForm

from .models import FormTestModel
from .models import PrivateTourFormModel
'''
class PrivateTourForm(forms.Form):

    des_beijing = forms.CharField(label='des_beijing', max_length=32)
    des_shanghai = forms.CharField(label='des_shanghai', max_length=32)

    car = forms.CharField(label='car', max_length=64)
    departure = forms.CharField(label='departure', max_length=64)
    nights = forms.CharField(label='nights', max_length=64)
    age1 = forms.CharField(label='age1', max_length=64)
    age2 = forms.CharField(label='age2', max_length=64)
    service1 = forms.CharField(label='service1', max_length=64)
    itinerary = forms.CharField(label='itinerary', max_length=512)

    fname = forms.CharField(label='fname', max_length=64)
    email = forms.CharField(label='email', max_length=64)
    country = forms.CharField(label='country', max_length=64)
'''
class PrivateTourForm(ModelForm):
    class Meta:
        model = PrivateTourFormModel
        fields = '__all__'


class PickupForm(forms.Form):
    location = forms.CharField(label='location', max_length=32)
    service = forms.CharField(label='service', max_length=32)
    car = forms.CharField(label='car', max_length=64)
    date = forms.CharField(label='date', max_length=64)
    flight = forms.CharField(label='flight', max_length=64)
    fname = forms.CharField(label='fname', max_length=64)
    email = forms.CharField(label='email', max_length=64)
    destination = forms.CharField(label='destination', max_length=512)

class TestForm(ModelForm):
    class Meta:
        model = FormTestModel
        fields = '__all__'
        #fields = ['fname', 'country']
