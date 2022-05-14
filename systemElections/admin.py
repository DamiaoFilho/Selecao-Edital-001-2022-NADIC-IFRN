from django.contrib import admin

from systemElections.models import Candidate, Election, Elector

# Register your models here.
admin.site.register(Candidate)
admin.site.register(Election)
admin.site.register(Elector)