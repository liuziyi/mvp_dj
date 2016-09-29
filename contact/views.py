from django.shortcuts import render
from django.views.generic.base import TemplateView 

from categories.models import Category 

class ContactView(TemplateView):
	template_name = "contact/contact.html"

	def get_context_data(self, **kwargs):
		context = super(ContactView, self).get_context_data(**kwargs)
		context["categories"] = Category.objects.all()
		return context
