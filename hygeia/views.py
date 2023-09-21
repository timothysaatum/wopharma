from django.shortcuts import render
from .models import Drug
from django.views.generic import (TemplateView, ListView, CreateView, 
										DeleteView, UpdateView, DetailView)




class HomeView(ListView):
	model = Drug
	template_name = 'hygeia/index.html'
	context_object_name = 'drugs'


def store(request):
	return render(request, 'hygeia/store.html')



class DrugDetailView(DetailView):
	model = Drug
	template_name = 'hygeia/drug_details.html'

def cart(request):
	return render(request, 'hygeia/cart.html')

def how_is_work(request):
	return render(request, 'hygeia/how_is_works.html')

def upload_prescription(request):
	return render(request, 'hygeia/upload_prescription.html')	
	