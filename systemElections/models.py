from itertools import count
from mimetypes import init
from msilib import init_database
import numbers
from pyexpat import model
from tkinter.tix import Balloon
from django.db import models
from django.urls import reverse
from django.db.models import Count
# Create your models here.

class Candidate(models.Model):
    cpf = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    birth = models.DateField()
    address = models.TextField()
    nElectors = models.IntegerField(default=0, blank=True)
    isWinner = models.BooleanField(default=False)
    Election = models.ForeignKey("Election", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('registerCandidate')
    
    """def att():
        x = Candidate.objects.annotate(number=Count('elector'))
        for i in x:
            if i.nElectors < i.number:
                i.nElectors += i.number
                i.save()
    """                

class Election(models.Model):
    id_Election = models.AutoField(primary_key=True)
    lawsuit = models.CharField(max_length=50)
    initDate = models.DateField()
    finalDate = models.DateField()
    isEnd = models.BooleanField(default=False)
    Winner = models.IntegerField(default=0, blank=True)
    nCandidates = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.lawsuit

    def get_absolute_url(self):
        return reverse('registerElection')

    def att():
        x = Election.objects.annotate(number=Count('candidate'))
        e = Election.objects.all()
        for i in e:
            for j in x:
                if(i.id_Election == j.id_Election):
                    i.nCandidates = j.number
                    i.save()
                    break
    

class Elector(models.Model):
    cpf = models.IntegerField(primary_key=True)
    Candidate = models.ForeignKey('candidate', on_delete=models.PROTECT)
    Election = models.ManyToManyField(Election)

    def __str__(self):
        return str(self.cpf)


