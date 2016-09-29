from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Event 

class EventListView(ListView):
	model = Event
	queryset = Event.objects.filter(start_date__year=2016).values()
