from bisect import bisect_right
from mimetypes import init
from pyexpat import model
from django.forms import ModelForm, ModelChoiceField, ModelMultipleChoiceField
from .models import *
from django import forms

class electorForm(forms.Form):

    model = Elector
    cpf = forms.IntegerField()


class candidateForm(forms.Form):
    models = Candidate
    cpf = forms.IntegerField()
    name = forms.CharField()
    birth = forms.DateField()
    address = forms.CharField()
    Election = forms.ModelChoiceField(Election.objects.all())

class electionForm(forms.Form):

    models = Candidate
    lawsuit = forms.CharField()
    initDate = forms.DateField()
    finalDate = forms.DateField()
    
 

