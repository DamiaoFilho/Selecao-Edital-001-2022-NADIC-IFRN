from bisect import bisect_right
from datetime import datetime
from pickle import NONE
from pyexpat import model
from select import select
from typing import final
from unicodedata import name
from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpRequest, request
from .models import *
from .forms import electorForm,candidateForm, electionForm
from datetime import date
# Create your views here.

def registerCandidate(request):
    Election.att()
    if request.method == 'GET':
        form = candidateForm()
        return render(request, 'systemElections/candidate_form.html', context = {'form': form})
    else:
        form = candidateForm(request.POST)
        if form.is_valid():
            cpf = form.cleaned_data.get("cpf")
            name = form.cleaned_data.get("name")
            birth = form.cleaned_data.get("birth")
            address = form.cleaned_data.get("address")
            Elections = form.cleaned_data.get("Election")
            obj = Candidate.objects.create(cpf = cpf, name = name, birth = birth, address = address, Election = Elections)
            obj.save()        

        return render(request, 'systemElections/candidate_form.html', context = {'form': form})

def registerElection(request):
    Election.att()
    if request.method == 'GET':
        form = electionForm()
        return render(request, 'systemElections/election_form.html', context = {'form': form})
    else:
        form = electionForm(request.POST)
        if form.is_valid():
            lawsuit = form.cleaned_data.get("lawsuit")
            initDate = form.cleaned_data.get("initDate")
            finalDate = form.cleaned_data.get("finalDate")
            obj = Election.objects.create(lawsuit = lawsuit, initDate = initDate, finalDate = finalDate)
            obj.save()        

        return render(request, 'systemElections/election_form.html', context = {'form': form})


def listElections(request):
    Election.att()
    Elections = Election.objects.all()
    for i in Elections:
        if(i.finalDate <= date.today()):
            i.isEnd = True
            obj = Candidate.objects.filter(Election = i.id_Election)
            x = 0
            for j in obj:
                if(j.nElectors >= x):
                    x = j.nElectors
                    i.Winner = j.cpf
                    i.save()
            win = Candidate.objects.get(cpf = i.Winner)
            win.isWinner = True
            win.save()

    return render(request, 'systemElections/election_list.html', {'election':Election.objects.filter(isEnd = False)})
    
def showCandidates(request, id):
    selected = Candidate.objects.filter(Election = id)
    return render(request, 'systemElections/candidate_list.html', context={'candidates' : selected})

def voteForm(request, id):
    if request.method == 'GET':
        form = electorForm()
        return render(request, 'systemElections/vote_form.html', context = {'voteForm': form})
    else:
        form = electorForm(request.POST)
        selectedCandidate = Candidate.objects.get(cpf = id)
        electors = Elector.objects.all()
        e = Election.objects.get(lawsuit = selectedCandidate.Election)
        if form.is_valid():
            cpf = form.cleaned_data.get("cpf")
            flag = True

            for i in electors:
                if i.cpf == cpf:
                    flag = False
                    f = True
                    for x in i.Election.all():
                        if x == e:
                            f = False
                            break
                            
                        
                    if f:
                        i.Election.add(e)
                        i.save()
                        selectedCandidate.nElectors += 1
                        selectedCandidate.save()
                        return redirect('listElections')

                    
            if flag:
                obj = Elector.objects.create(cpf=cpf, Candidate=selectedCandidate)
                obj.save()
                obj.Election.add(e)
                selectedCandidate.nElectors += 1
                selectedCandidate.save()
                return redirect('listElections')
        return render(request, 'systemElections/vote_form.html', context = {'voteForm': form})

def listEndedElections(request):
    e = Election.objects.filter(isEnd = True)
    c = Candidate.objects.filter(isWinner = True)
    return render (request, 'systemElections/list_ended_elections.html', context = {'election':e, 'candidate':c})

    
