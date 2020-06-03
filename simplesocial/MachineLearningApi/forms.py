from django import forms
# from .models import Post
from django.conf import settings
from django.db import models
from django.utils import timezone

from django import forms
from django.forms import ModelForm
from .models import UserDetails,dataCleaningModels,replaceNaNvaluesModels


class UserModelForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = "__all__" 

class dataCleaningForm(forms.ModelForm):
    class Meta:
        model = dataCleaningModels
        fields = "__all__" 

class replaceNaNvaluesModelsForm(forms.ModelForm):
    class Meta:
        model = replaceNaNvaluesModels
        fields = "__all__" 

class EventsForm(forms.Form):
    docfile = forms.FileField(
        label="Select a File",
        help_text="Max. 42 megabytes"
    )

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


