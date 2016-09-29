from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Result, ResultDetail

class ResultListView(ListView):
	model = Result
	queryset = Result.objects.all().values() 

class ResultDetailView(DetailView):
	model = Result

	def get_context_data(self, **kwargs):
		context = super(ResultDetailView, self).get_context_data(**kwargs)
		context["result_details"] = Result.objects.get(pk=kwargs.get("object").id).resultdetail_set.all().values()
		return context
