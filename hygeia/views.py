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

def herbal_medicine(request):
	return render(request, 'hygeia/herbal_medicine.html')

def sundries(request):
	return render(request, 'hygeia/sundries.html')

def cosmetics(request):
	return render(request, 'hygeia/cosmetics.html')

def vitamins(request):
	return render(request, 'hygeia/vitamins.html')

def snacks_confec(request):
	return render(request, 'hygeia/snacks_confec.html')

def baby_food(request):
	return render(request, 'hygeia/baby_food.html')

def sex_enhance(request):
	return render(request, 'hygeia/sex_enhance.html')

def pharmacies(request):
	return render(request, 'hygeia/pharmacies.html')

def book_consult(request):
	return render(request, 'hygeia/book_consult.html')

def drug_details_page(request):
	return render(request, 'hygeia/drug_details_page.html')

def checkout(request):
	return render(request, 'hygeia/checkout.html')

def cart_page(request):
	return render(request, 'hygeia/cart_page.html')

def consultation(request):
	return render(request, 'hygeia/consultation.html')

def specialist(request):
	return render(request, 'hygeia/specialist.html')				

	