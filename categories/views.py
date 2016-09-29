from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 

from .models import Category 

class CategoryListView(ListView):
	model = Category

	def get_context_data(self, **kwargs):
		context = super(CategoryListView, self).get_context_data(**kwargs)
		context["categories"] = Category.objects.all()
		return context

class CategoryDetailView(DetailView):
	model = Category
