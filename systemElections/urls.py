from unicodedata import name
from django.urls import path
from .views import *


urlpatterns = [
    path('cadastrarCandidato/', registerCandidate, name='registerCandidate'),
    path('cadastrarEleicao/', registerElection, name='registerElection'),
    path('listaEleicao/', listElections, name='listElections'),
    path('showCandidates/<int:id>', showCandidates, name='showCandidates'),
    path('voteForm/<int:id>', voteForm, name='vote'),
    path('vencedores', listEndedElections, name='listEndedElections')
]